"""
Convenience functions for reading and writing files of different types: text,
pickle, json, etc.
"""
# !EXPORT_TO_README
import csv
import io
import json
import os
import platform
import sys
import tempfile
import warnings
import dataclasses
from itertools import count
from functools import partial
from typing import cast, Dict, Iterable, List, Optional, Sequence, Tuple, Type, TypeVar, Union, Any, Callable, IO

from mhelper import array_helper, exception_helper, file_helper, string_helper, enum_helper
from mhelper.special_types import NOT_PROVIDED

T = TypeVar( "T" )
U = TypeVar( "U" )
TIniSection = Dict[str, str]
TIniData = Dict[str, TIniSection]

TPathLike = Union[os.PathLike, str]


def read_all_text( *args, **kwargs ) -> Optional[str]:
    """
    See `read_all_data`.
    """
    return read_all_data( *args, **kwargs, binary = False )


def read_all_bytes( *args, **kwargs ) -> Optional[bytes]:
    """
    See `read_all_data`.
    """
    return read_all_data( *args, **kwargs, binary = True )


def read_all_data( file_name: str,
                   default: Optional[str] = NOT_PROVIDED,
                   *,
                   details: str = None,
                   binary: bool = False
                   ) -> Optional[Union[str, bytes]]:
    """
    Reads all the text from a file, returning None if there is no file
    
    Supports additional features, see `open2`.
    
    :param file_name: Path to file to read
    
    :param default:   Default value if file does not exist.
                      If `NOT_PROVIDED` then a `FileNotFoundError` is raised.
                      
    :param details:   Appended to any `FileNotFoundError` error message.
    
    :param binary:    Read bytes, not `str`.
    
    :except FileNotFoundError: File does not exist and no default has been provided. 
    """
    file_name = file_helper.normalise_path( file_name )

    if not os.path.isfile( file_name ):
        if default is NOT_PROVIDED:
            raise FileNotFoundError(
                "Cannot read_all_text from file because the file doesn't exist: «{}».{}".format( file_name, (
                    " Description of file: {}.".format( details )) if details else "" ) )

        return default

    with open2( file_name, binary = binary ) as file:
        return file.read()


def read_all_lines( file_name: str ) -> List[str]:
    """
    See `read_all_data`.
    """

    if not os.path.isfile( file_name ):
        raise FileNotFoundError( "The file «{}» does not exist.".format( file_name ) )

    with open2( file_name ) as file:
        return list( x.rstrip( "\n" ) for x in file )


class open2:
    """
    All-purpose `open`
    
    * Handles GZipped streams for ".gz" extensions.
    * Assumes text is UTF8-encoded by default, even on Windows.
    * When writing, uses an temporary, intermediate file to avoid partially
      written files should the program crash.
    """

    def __init__( self,
                  file_name: TPathLike,
                  binary = False,
                  gzip: Optional[bool] = None,
                  write: bool = False ):
        """
        :param file_name:   File name 
        :param binary:      Open in binary mode 
        :param gzip:        Pass through Gzip.
                            If `None` uses the file extension. 
        :param write:       Open in write mode. 
        """
        self.file_name = file_name
        self.binary = binary
        self.gzip = os.fspath(file_name).lower().endswith( ".gz" ) if gzip is None else gzip
        self.write = write
        self.__close_stack = []

    def __enter__( self ) -> IO:
        file_name = os.fspath( self.file_name)
        
        if self.write:
            intermediate = use_intermediate( file_name )
            file_name = self.__stack( intermediate )
            mode = "w"
        else:
            mode = "r"

        if self.gzip:
            import gzip
            h_gzip = gzip.open( file_name, mode )
            self.__stack( h_gzip )

            if self.binary:
                return h_gzip
            else:
                h_io = io.TextIOWrapper( h_gzip, encoding = "utf8" )
                return self.__stack( h_io )
        else:
            if self.binary:
                h_file = open( file_name, f"{mode}b" )
            else:
                h_file = open( file_name, mode, encoding = "utf8" )

            return self.__stack( h_file )

    def __exit__( self, exc_type, exc_val, exc_tb ):
        while self.__close_stack:
            self.__close_stack.pop( -1 ).__exit__( exc_type, exc_val, exc_tb )

    def __stack( self, x ):
        self.__close_stack.append( x )
        return x.__enter__()


open_for_read = open2
open_for_write = partial( open2, write = True )


def write_all_bytes( file_name: os.PathLike, data: bytes ) -> None:
    """
    Writes binary data.
    
    Supports additional features, see `open2`.
    """
    with open2(  file_name , write = True, binary = True ) as file:
        file.write( data )


def write_all_text( file_name: TPathLike, text: Union[Sequence[str], str], newline: bool = False,
                    join: str = "\n" ) -> None:
    """
    Writes text data.
    
    Supports additional features, see `open2`.
    
    :param file_name:       Target 
    :param text:            Text, or a sequence of lines 
    :param newline:         Adds a newline at the end of the text (if a sequence
                            is provided). 
    :param join:            Character used to join lines (if a sequence is 
                            provided).
    """
    from mhelper import array_helper

    if array_helper.is_simple_iterable( text ):
        text = join.join( text )

        if newline:
            text += "\n"

    with open2(  file_name , write = True ) as file:
        file.write( text )


# noinspection PyPackageRequirements
def load_npy( file_name ):
    """
    Loads an NPY file. If it is an NPZ this extracts the `data` value automatically.
    Requires the :library:`numpy`.
    """

    import numpy
    result = numpy.load( file_name, allow_pickle = False, fix_imports = False )

    if file_name.upper().endswith( ".NPZ" ):
        result = result["data"]

    return result


def load_npz( file_name ):
    """
    Loads an NPZ file and returns the `data` value.
    Requires the :library:`numpy`.
    """

    # noinspection PyPackageRequirements
    import numpy
    result = numpy.load( file_name, allow_pickle = False, fix_imports = False )
    result = result["data"]

    return result


class TsvReader:
    class __Actor:
        class __Row:
            __slots__ = "owner", "row"

            def __init__( self, owner, row ):
                self.owner = owner
                self.row = row

            def __getitem__( self, item ):
                if isinstance( item, int ):
                    return self.row[item]
                elif isinstance( item, str ):
                    return self.row[self.owner.get_column( item )]
                else:
                    raise exception_helper.type_error( "item", item, Union[str, int] )

            def to_tsv( self, delimiter = "\t" ):
                return delimiter.join( self.row )

            def __repr__( self ):
                return f"{self.__class__.__qualname__}({{ k: v for k, v in zip( self.owner.headers, self.row ) }})"

        __slots__ = "owner", "fin", "reader", "headers", "is_closed"

        def __init__( self, owner: "TsvReader" ):
            self.owner: TsvReader = owner
            self.fin: IO = open( owner.file_name )

            kwargs = self.owner.kwargs
            kwargs.setdefault( "delimiter", "\t" )

            self.reader: csv.reader = csv.reader( self.fin, **kwargs )
            self.headers: Dict[str, int] = array_helper.create_index_lookup( next( self.reader ) )
            self.is_closed: bool = False

        def get_column( self, name ):
            try:
                return self.headers[name]
            except KeyError as ex:
                headers = set( self.headers )
                raise KeyError( f"No such header as {name!r} in {headers!r}" ) from ex

        def __iter__( self ):
            return self

        def __next__( self ):
            row = next( self.reader )  # ~~> StopIteration

            return self.__Row( self, row )

        def _close( self ):
            if self.is_closed:
                raise ValueError( "File is already closed." )

            self.fin.close()
            self.is_closed = True

    __slots__ = "file_name", "__actor", "kwargs"

    def __init__( self, file_name, **kwargs ):
        self.file_name = file_name
        self.kwargs = kwargs
        self.__actor = None

    def __enter__( self ) -> __Actor:
        assert self.__actor is None
        self.__actor = self.__Actor( self )
        return self.__actor

    def __exit__( self, exc_type, exc_val, exc_tb ):
        assert self.__actor is not None
        self.__actor._close()


def save_bitarray( file_name: str, value ) -> None:
    """
    Saves a bit array.
    Requires the :library:`bitarray`.
    
    :type value: bitarray
    
    :param file_name: File name
    :param value: Value to save
    """
    try:
        # noinspection PyPackageRequirements
        from bitarray import bitarray
    except ImportError as ex:
        raise ImportError( "save_bitarray requires the bitarray package." ) from ex

    from mhelper import exception_helper, file_helper

    exception_helper.assert_instance( "save_bitarray::value", value, bitarray )
    assert isinstance( value, bitarray )

    try:
        with open( file_name, "wb" ) as file_out:
            value.tofile( file_out )
    except TypeError:
        # Stupid "open file expected" error on OSX (due to bug writing large files - fallback to manual implementation)
        _save_bytes_manually( file_name, value.tobytes() )
    except Exception as ex:
        raise ValueError( "Failed to write bitarray of length {} to «{}».".format( len( value ), file_name ) ) from ex

    size = float( file_helper.file_size( file_name ) )
    expected = len( value )

    if size < expected / 8.0:
        raise ValueError(
            "Saved file is shorter ({} bytes or {} bits) than the originating bitarray ({} bytes or {} bits).".format(
                size, size * 8, expected / 8, expected ) )


def _save_bytes_manually( file_name: str, value: bytes ):
    """
    Fallback function used by :func:`save_bitarray`.
    """
    warnings.warn(
        "Save bitarray failed. This is probably due to an error in your `bitarray` library. The file will be saved incrementally but this will take longer.",
        UserWarning )
    BATCH_SIZE = 100000
    cursor = 0
    length = len( value )

    with open( file_name,
               "wb" ) as file_out:  # note that writing large arrays on OSX is probably the problem, we can't just dump the bytes
        while cursor < length:
            next = min( cursor + BATCH_SIZE, length )
            slice = value[cursor:next]
            file_out.write( slice )
            cursor = next


def _read_bytes_manually( file_name: str ) -> bytes:
    BATCH_SIZE = 100000
    b = bytearray()

    with open( file_name, "rb" ) as file_in:
        while True:
            buf = file_in.read( BATCH_SIZE )

            if len( buf ) == 0:
                break

            b.extend( buf )

    return bytes( b )


def load_bitarray( file_name: str ):
    """
    Loads a bitarray
    :param file_name: File to read 
    :return: bitarray. Note this may be padded with missing bits. 
    """
    try:
        # noinspection PyPackageRequirements
        from bitarray import bitarray
    except ImportError as ex:
        raise ImportError( "save_bitarray requires the bitarray package." ) from ex

    result = bitarray()

    try:
        with open( file_name, 'rb' ) as file_in:
            result.fromfile( file_in )
    except SystemError:  # OSX error
        result = bitarray()
        result.frombytes( _read_bytes_manually( file_name ) )
        assert len( result ) != 0

    return result


# noinspection PyPackageRequirements
def save_npy( file_name, value ):
    import numpy

    numpy.save( file_name, value, allow_pickle = False, fix_imports = False )


# noinspection PyPackageRequirements
def save_npz( file_name, value ):
    import numpy

    numpy.savez_compressed( file_name, data = value )


def SequentialReader( *args, **kwargs ):
    from mhelper import sequential_io
    return sequential_io.SequentialReader( *args, **kwargs )


def SequentialWriter( *args, **kwargs ):
    from mhelper import sequential_io
    return sequential_io.SequentialWriter( *args, **kwargs )


def load_binary( file_name: str,
                 *,
                 type_: Optional[Union[type, Type[T], Sequence]] = None,
                 default: U = NOT_PROVIDED,
                 delete_on_fail = False,
                 values: int = 0,
                 warn: bool = False ) -> Union[T, U]:
    """
    Loads a binary file
    
    :param warn:            Warn on deserialisation errors, even if a default is
                            provided.
    :param delete_on_fail:  Show a warning and recycle the file if *any* value
                            cannot be retrieved.
    :param file_name:       Filename to load  
    :param type_:           Type            --> Type to expect for every item
                            Sequence[Type]  --> Type to expect for each item
                            None            --> Perform no check
    :param default:         object           --> Value to default all item(s) to
                            Sequence[object] --> Value to default each item to
                            `NOT_PROVIDED`   --> Raise error on missing value 
    :param values:          Number of values to deserialise.
                            0 --> Length of `type_`
                            1 --> Result is the single object deserialised
                            2 --> Result is a list of objects deserialised
                            
    :return: Loaded data, or a sequence of loaded data.
    
    :except ValueError: Deserialisation of any default `NOT_PROVIDED` failed. 
    """

    if values == 0:
        if isinstance( type_, list ) or isinstance( type_, tuple ):
            values = len( type_ )
        else:
            values = 1
            type_ = [type_]

    if not isinstance( type_, list ) and not isinstance( type_, tuple ):
        type_ = [type_] * values

    if not isinstance( default, list ) and not isinstance( default, tuple ):
        default = [default] * values

    assert len( type_ ) == len( default ) == values

    import pickle

    result = []
    failures = []

    try:
        with open( file_name, "rb" ) as file:
            for item_index, item_type, item_default in zip( count(), type_, default ):
                try:
                    item_value = pickle.load( file, fix_imports = False )

                    if item_type is not None:
                        if not isinstance( item_value, item_type ):
                            raise ValueError(
                                f"Deserialised object #{item_index} from file «{file_name}» was expected to be of type «{item_type}» but it's not, its of type «{type( result )}» with a value of «{result}»." )
                except Exception as ex:
                    failure = ex
                    item_value = item_default
                else:
                    failure = None

                failures.append( failure )
                result.append( item_value )
    except Exception as ex:
        failures = [ex]
        result = default

    if any( failures ):
        if delete_on_fail:
            warnings.warn( "\n"
                           "************************************************************\n"
                           "* Failed to load binary file due to an error:              *\n"
                           "************************************************************\n"
                           "* This is probably due to a version incompatibility        *\n"
                           "* You may need to recreate this file.                      *\n"
                           "* The problematic file has been sent to the recycle bin.   *\n"
                           "* If it is important, please retrieve it now.              *\n"
                           "************************************************************\n"
                           "* Error: {} : {}\n"
                           "* File : {}\n"
                           .format( type( failure ).__name__, failure, file_name ), UserWarning )
            file_helper.recycle_file( file_name )

        if any( x is NOT_PROVIDED for x in result ):
            raise ValueError( f"Failed to deserialise '{file_name}'." ) from failures[0]

        if warn:
            warnings.warn( f"At least one problem occured deserialising '{file_name}': {failures}" )

    if len( result ) == 1:
        return result[0]
    else:
        return result


def save_binary( file_name: Optional[str], value = None, *, values = None ) -> Optional[bytes]:
    """
    Saves a binary file.
    
    * Uses an intermediate for safe writing
        
    :param file_name:       Target file. If this is `None` the bytes are returned instead of being
                            saved.
    :param value:           Value to store 
    :param values:          Alternative to `value` that. This should be a list or tuple indicating 
                            a series of values to store sequentially. 
    :return:                Bytes if `file_name` is `None`, else `None`.
    """
    import pickle

    if values is None:
        values = [value]
    elif value is not None:
        raise ValueError( "Cannot specify both `value` and `values`." )

    if file_name is None:
        try:
            r = []
            for value in values:
                r.append( pickle.dumps( value, protocol = -1, fix_imports = False ) )
            return b"".join( r )
        except Exception as ex:
            raise IOError( "Error saving data to bytes. Data = «{}».".format( value ) ) from ex

    with use_intermediate( file_name ) as inter_name:
        with open( inter_name, "wb" ) as file:
            for value in values:
                try:
                    pickle.dump( value, file, protocol = -1, fix_imports = False )
                except Exception as ex:
                    raise IOError( f"Error saving data to binary file. Filename = {inter_name!r}." ) from ex

    return None


_lock_warning = True


def load_json_data( file_name, default = NOT_PROVIDED ):
    import json

    if (not file_name or not os.path.isfile( file_name )) and default is not NOT_PROVIDED:
        return default

    try:
        with open( file_name, "r" ) as file_in:
            return json.load( file_in )
    except Exception as ex:
        raise ValueError( f"Could not load JSON file '{file_name}'." ) from ex


def save_json_data( file_name, value, pretty = False ):
    import json

    with write_intermediate( file_name ) as file_out:
        if pretty:
            return json.dump( value, file_out, indent = 4 )
        else:
            return json.dump( value, file_out, separators = (',', ':') )


# noinspection PyUnresolvedReferences
def load_json_pickle( file_name, keys = True, default = NOT_PROVIDED ):
    from mhelper.file_helper import read_all_text
    import jsonpickle

    if default is not NOT_PROVIDED and not os.path.isfile( file_name ):
        return default

    text = read_all_text( file_name )

    return jsonpickle.decode( text, keys = keys )


# noinspection PyUnresolvedReferences
def save_json_pickle( file_name, value, keys = True ):
    from mhelper.file_helper import write_all_text
    import jsonpickle

    write_all_text( file_name, jsonpickle.encode( value, keys = keys ) )


def default_values( target: T, default: Optional[Union[T, type]] = None ) -> T:
    if default is None:
        if target is None:
            raise ValueError(
                "Cannot set the defaults for the value because both the value and the defaults are `None`, so neither can be inferred." )

        default = type( target )

    if isinstance( default, type ):
        default = default()

    if target is None:
        return default

    if isinstance( target, list ):
        # noinspection PyTypeChecker
        return cast( T, target )

    if type( target ) is not type( default ):
        raise ValueError(
            "Attempting to set the defaults for the value «{}», of type «{}», but the value provided, «{}», of type «{}», is not compatible with this.".format(
                target, type( target ), default, type( default ) ) )

    added = []
    replaced = []
    removed = []

    for k, v in default.__dict__.items():
        if k.startswith( "_" ):
            continue

        if k not in target.__dict__:
            added.append( k )
            target.__dict__[k] = v
        elif type( target.__dict__[k] ) != type( v ):
            replaced.append( k )
            target.__dict__[k] = v

    to_delete = []

    for k in target.__dict__.keys():
        if k not in default.__dict__:
            to_delete.append( k )

    for k in to_delete:
        removed.append( k )
        del target.__dict__[k]

    return target


def open_write_doc( map = None, wrap = 78, allow_files: bool = True, allow_blank: bool = True, *,
                    metavar: str = "TARGET" ):
    warnings.warn( "Deprecated - use output_helper.TargetWriter.document", DeprecationWarning )
    from mhelper import output_helper
    return output_helper.TargetWriter( map = map, wrap = wrap, allow_files = allow_files, allow_blank = allow_blank,
                                       metavar = metavar ).document()


def open_write( file_name: str,
                extension: str = "",
                mode: type = str,
                map = None,
                create: bool = True,
                intermediate: bool = True,
                allow_files: bool = True,
                allow_blank: bool = True ):
    warnings.warn( "Deprecated - use output_helper.TargetWriter.open", DeprecationWarning )
    from mhelper import output_helper
    return output_helper.TargetWriter( map = map, create = create, use_intermediate = intermediate,
                                       allow_files = allow_files, allow_blank = allow_blank ).open(
        file_name = file_name, extension = extension, mode = mode )


def load_ini( file_name: str, comments: str = (";", "#", "//"), stop: Tuple[str, str] = None ) -> Dict[
    str, Dict[str, str]]:
    """
    Loads an INI file.
    
    :param file_name:       File to load 
    :param stop:            When this section and key are encountered, reading the INI stops with
                            whatever has been loaded so far.
    :param comments:        Comment lines 
    :return:                INI data:
                                str - Section name ("" contains the data from any untitled section or sections with no name `[]`)
                                dict - Section data:
                                    str - Field key
                                    str - field value
    """

    with open( file_name, "r" ) as fin:
        return load_ini_str( fin,
                             comments,
                             stop )


def load_ini_str( fin: Union[str, Iterable[str]],
                  comments: str = (";", "#", "//"),
                  stop: Tuple[str, str] = None ) -> Dict[str, Dict[str, str]]:
    if isinstance( fin, str ):
        fin = fin.split( "\n" )

    r = {}
    unsectioned = {}
    section = unsectioned
    section_name = ""

    for line in fin:
        line = line.strip()

        if any( line.startswith( x ) for x in comments ):
            continue

        if line.startswith( "[" ) and line.endswith( "]" ):
            section = {}
            section_name = line[1:-1]
            r[section_name] = section
        elif "=" in line:
            k, v = line.split( "=", 1 )
            section[k.strip()] = v.strip()

            if stop is not None and stop[0] == section_name and stop[1] == k:
                break

    if unsectioned:
        if "" in r:
            unsectioned.update( r[""] )

        r[""] = unsectioned

    return r


def save_ini( file_name: str, data: Dict[str, Dict[str, str]] ) -> None:
    with open( file_name, "w" ) as file:
        if "" in data:
            __write_ini_section( data[""], file )

        for section, fields in data.items():
            if section:
                file.write( "[{}]\n".format( section ) )
                __write_ini_section( fields, file )


def __write_ini_section( fields, file ):
    for name, value in fields.items():
        file.write( "{}={}\n".format( name, value ) )
    file.write( "\n" )


class queue_delete:
    """
    The file will be deleted when the program closes.
    
    If the program force-closes then the file is not deleted.
    
    :remarks:           Class masquerading as function.
                        
                        Example usage:
                            ```
                            queue_delete( "c:\my_temporary_file.txt" )
                            ```    
    
    :cvar queued:       Gets the list of files to be deleted.
                        Acts to keep the references alive until the program closes.
    :ivar file_name:    Name of the file
    """

    queued = []

    def __init__( self, file_name: str ) -> None:
        """
        CONSTRUCTOR
        Automatically adds the reference to the queue, keeping it alive
        until the program closes.
        
        :param file_name: Name of the file
        """
        self.file_name = file_name
        self.queued.append( self )

    def __del__( self ) -> None:
        """
        !OVERRIDE
        On deletion, removes the file.
        """
        os.remove( self.file_name )


class with_temporary:
    """
    The file will be deleted when the with block ends
    """

    def __init__( self, file_name: str = None, *, condition: bool = True ):
        """
        Names a file that is deleted when the with block ends.
        
        :param file_name:   A filename (not starting `.`), an extension of a new
                            temporary file (starting `.`), or `None`, for an
                            extension-less temporary file. 
        """
        if not file_name or file_name.startswith( "." ):
            file_name = tempfile.NamedTemporaryFile( "w",
                                                     delete = False,
                                                     suffix = file_name ).name

        self.file_name = file_name
        self.condition = condition

    def __enter__( self ):
        """
        `with` returns the filename.
        """
        return self.file_name

    def __exit__( self, exc_type, exc_val, exc_tb ):
        """
        End of `with` deletes the file.
        """
        if self.condition:
            try:
                os.remove( self.file_name )
            except FileNotFoundError as ex:
                raise FileNotFoundError( "Failed to delete file '{}'.".format( self.file_name ) ) from ex


with_delete = with_temporary


class ESystem:
    UNKNOWN = 0
    WINDOWS = 1
    MAC = 2
    LINUX = 3


def get_system():
    s = platform.system()
    if s == "Windows":
        return ESystem.WINDOWS
    elif s == "Darwin":
        return ESystem.MAC
    elif s == "Linux":
        return ESystem.LINUX
    else:
        return ESystem.UNKNOWN


def system_open( file_name: str ):
    """
    Opens the file with the default editor.
    (Only works on Windows, Mac and GUI GNU/Linuxes)
    """
    s = platform.system()
    if s == "Windows":
        os.system( file_name )
    elif s == "Darwin":
        os.system( "open \"" + file_name + "\"" )
    elif s == "Linux":
        os.system( "xdg-open \"" + file_name + "\"" )
    else:
        warnings.warn( "I don't know how to open files with the default editor on your platform '{}'.".format( s ) )


def system_select( file_name: str ):
    """
    Selects the file with the default file explorer.
    (Only works on Windows, Mac and GUI Linuxes)
    """
    s = platform.system()
    if s == "Windows":
        os.system( "explorer.exe /select,\"{}\"".format( file_name ) )
    elif s == "Darwin":
        os.system( "open -R \"{}\"".format( file_name ) )
    elif s == "Linux":
        # Just open the parent directory on Linux
        file_name = os.path.split( file_name )[0]
        os.system( "xdg-open \"{}\"".format( file_name ) )
    else:
        warnings.warn( "I don't know how to open files with the default editor on your platform '{}'.".format( s ) )


def hash_file( file_name: str, algorithm = "sha256" ) -> str:
    import hashlib
    sha1 = getattr( hashlib, algorithm )()
    BUF_SIZE = 10000

    with open( file_name, 'rb' ) as f:
        while True:
            data = f.read( BUF_SIZE )
            if not data:
                break
            sha1.update( data )

    return sha1.hexdigest()


def system_cls():
    """
    Clears the terminal display.
    
    .. note::
    
        The proper way is to send the correct ANSI sequence, however in practice this produces odd results.
        So we just use the specific system commands.
        Note that we send two ``clear``s for Unix - once doesn't fully clear the display. 
    """
    if sys.platform.lower() == "windows":
        os.system( "cls" )
    else:
        os.system( "clear ; clear" )


def gzip( in_file_name: str,
          out_file_name: Optional[str] = None,
          overwrite: Optional[bool] = None,
          compress: bool = True
          ) -> str:
    """
    Zips or un-gzips a file.
    
    An intermediate file is used, so the output file is always guaranteed to be
    complete. 
    
    :param in_file_name:    Input file.
                            This is not deleted. 
                            
    :param out_file_name:   Output file.
                            If `None` then `in_file_name` is used, plus or minus a `.gz` extension.
                            
    :param overwrite:       `True` --> if the output exists, it will be overwritten
                            `False` --> if the output exists, take no action.
                            `None` --> if the output exists, raise an exception
                            
    :param compress:        When set, compresses, when unset, decompresses.
                              
    :return:                Output file name. 
    """
    if out_file_name is None:
        if compress:
            out_file_name = in_file_name + ".gz"
        else:
            if file_helper.get_extension( in_file_name ).lower() != ".gz":
                raise ValueError(
                    "Cannot generate the name of the Gzip decompressed file from the name of a compressed file ('{}') that does not end in '.gz'.".format(
                        in_file_name ) )

            out_file_name = file_helper.get_full_filename_without_extension( in_file_name )

    if os.path.isfile( out_file_name ):
        if overwrite is None:
            raise FileExistsError(
                "The output file already exists for the gzip/ungzip operation '{}' --> '{}'.".format( in_file_name,
                                                                                                      out_file_name ) )
        elif not overwrite:
            return out_file_name

    with use_intermediate( out_file_name ) as intermediate_file_name:
        import gzip
        import shutil

        if compress:
            with open( in_file_name, "rb" ) as f_in:
                with gzip.GzipFile( intermediate_file_name, "wb", mtime = 0 ) as f_out:
                    shutil.copyfileobj( f_in, f_out )
        else:
            with gzip.open( in_file_name, "rb" ) as f_in:
                with open( intermediate_file_name, "wb" ) as f_out:
                    shutil.copyfileobj( f_in, f_out )

    return out_file_name


ungzip = partial( gzip, compress = False )


class EnumJsonEncoder( json.JSONEncoder ):
    """
    Json encoder supporting enums (written as strings)::
    
        "EnumName::EnumValue"
    
    Note that, during decoding, strings that look like enums will be converted
    into enums, that is::
    
        "EnumName::*"
        
    For any ``EnumName`` in the `supported_enums`.
    If ``*`` cannot be found in the values of that enum, an error is raised.
    
    The prefix can be disabled. This will only decode successfully if the enum
    type can be determined because `EnumJsonDecoder`\'s `supported_enums`
    mentions the field names, or conducts a full `search`. 
    """

    def __init__( self, *args, supported_enums, prefix: bool = True, **kwargs ):
        super().__init__( *args, **kwargs )
        self.supported = set( supported_enums )
        self.prefix = prefix

    def default( self, o ):
        if type( o ) in self.supported:
            if self.prefix:
                return f"{type( o ).__name__}::{o.name}"
            else:
                return o.name

        return super().default( o )


class EnumJsonDecoder( json.JSONDecoder ):
    """
    Counterpart of `EnumJsonEncoder`.
    """

    def __init__( self, *args, supported_enums, search: bool = False, **kwargs ):
        """
        :param args: 
        :param supported_enums: A list of supported enum types.
                                *OR*
                                A dict mapping supported enum types to the names
                                of variables holding values of those types. 
        :param search:          Allow enum names to be missing - only works for unambiguous enums.
        :param kwargs: 
        """
        super().__init__( *args, object_hook = self.__object_hook, **kwargs )
        self.supported = {klass.__name__: klass for klass in supported_enums}

        if isinstance( supported_enums, dict ):
            self.map = {vv: k for k, v in supported_enums.items() for vv in v}
        else:
            self.map = None

        if search:
            self.search = {}

            for e in supported_enums:
                for em in e:
                    if em.name in self.search:
                        raise ValueError(
                            f"Cannot use `search` with this EnumJsonDecoder because the enum name '{em.name}' is ambiguous between {em} and {self.search[em.name]}." )
                    else:
                        self.search[em.name] = em

    def __object_hook( self, s ):
        u = {}

        for k, v in s.items():
            if not isinstance( v, str ):
                continue

            if "::" in v:
                # Explicit name
                klass_n, name = v.split( "::", 1 )
                klass = self.supported.get( klass_n )

                if klass is not None:
                    u[k] = klass[name]
            elif self.map is not None and k in self.map:
                # Field name in map
                klass = self.map.get( k )
                u[k] = klass[v]
            elif self.search is not None and v in self.search:
                # Full search
                if self.search[v] is None:
                    raise ValueError(
                        "This enum name cannot be converted back to an enum because it is ambiguous. Please state the enum name explicitly in the JSON, or provide the field name for this enum type to the JSON decoder." )

                u[k] = self.search[v]

        s.update( u )

        return s


# region Deprecated

def load_json( file_name, keys = True, default = NOT_PROVIDED ):
    warnings.warn( "Ambiguous - use load_json_data or `load_json_pickle`", DeprecationWarning )
    return load_json_pickle( file_name, keys = keys, default = default )


def save_json( file_name, value, keys = True ):
    warnings.warn( "Ambiguous - use save_json_data or `save_json_pickle`", DeprecationWarning )
    return save_json_pickle( file_name, value, keys = keys )


# endregion

def iter_file_lines( fin ):
    """
    Like `iter(FileIO)` (i.e. `FileIO.__next__`), but doesn't disable 
    `FileIO.tell`.
    """
    while True:
        line = fin.readline()

        if not line:
            break

        yield line


def get_temporary_file( extension = ".tmp" ):
    file = tempfile.NamedTemporaryFile( "w", delete = False, suffix = extension )
    file.close()
    name = file.name
    queue_delete( name )
    return name


class use_intermediate:
    """
    A variant of `write_intermediate` that doesn't open the file and 
    returns the filename instead.
    
    An error is raised if the intermediate has not been created by the time the
    ``with`` block ends.
    
    
    """
    __slots__ = "__file_name", "__i_file_name", "_stage"

    def __init__( self, file_name ):
        self.__file_name = file_name
        self.__i_file_name = self.__file_name + ".~intermediate"
        self._stage = 0

    def __enter__( self ):
        assert self._stage == 0
        self._stage = 1
        return self.__i_file_name

    def __exit__( self, exc_type, exc_val, exc_tb ):
        assert self._stage == 1

        if exc_val is not None:
            if os.path.isfile( self.__i_file_name ):
                os.remove( self.__i_file_name )

            return

        if not os.path.isfile( self.__i_file_name ):
            raise RuntimeError(
                f"`use_intermediate` ({self.__file_name!r}) expected the intermediate file ({self.__i_file_name!r}) to have been created, but is has not." )

        os.replace( self.__i_file_name, self.__file_name )

        self._stage = 2

    def __repr__( self ):
        return f"{self.__class__.__name__}({self.__file_name!r}, {self.__i_file_name}, {self._stage})"


class write_intermediate:
    """
    Opens a temporary file for writing.
    When closed, the temporary file is renamed to the target.
    This avoids the problem where a program closes before it completes its
    output, leaving the user (or another program) unsure if the output file
    is complete or partial.
    
    Usage is the same as `open` (though note that writing through an
    intermediate implicitly prevents read/append modes).
    
    Unlike `open`, instances of this class enforce enter/exit semantics.
    """
    __slots__ = "__file_name", "__i_file_name", "__stage", "__mode", "__handle", "__device"

    def __init__( self, file_name, mode = "w" ):
        self.__file_name = file_name
        self.__stage = 0
        self.__mode = mode
        self.__handle = None
        self.__device = file_name.startswith( "/dev/" )

        if self.__device:
            self.__i_file_name = os.path.expanduser(
                "~/.mhelper_io_helper_temporary_file_" + string_helper.get_random_alphanumeric( 16 ) )
        else:
            self.__i_file_name = self.__file_name + ".~intermediate"

    def __enter__( self ):
        assert self.__stage == 0
        if "b" in self.__mode:
            self.__handle = open( self.__i_file_name, self.__mode )
        else:
            self.__handle = open( self.__i_file_name, self.__mode, encoding = "utf8" )

        self.__stage = 1
        return self.__handle.__enter__()

    def __exit__( self, exc_type, exc_val, exc_tb ):
        assert self.__stage == 1

        self.__handle.__exit__()

        if exc_val is not None:
            if os.path.isfile( self.__i_file_name ):
                os.remove( self.__i_file_name )

            return

        if not os.path.isfile( self.__i_file_name ):
            # Intermediate *not* created
            raise RuntimeError(
                f"`use_intermediate` ({self.__file_name!r}) expected the intermediate file ({self.__i_file_name!r}) to have been created, but is has not." )

        if self.__device:
            # Write to device
            try:
                with open( self.__i_file_name, "r", encoding = "utf8" ) as fin:
                    with open( self.__file_name, "w", encoding = "utf8" ) as fout:
                        for line in fin:
                            fout.write( line )
            finally:
                os.remove( self.__i_file_name )
        else:
            # Move normally
            os.replace( self.__i_file_name, self.__file_name )

        self.__stage = 2


# noinspection PyDataclass
def save_tsv( file_name: str,
              content: Any,
              header: Any = True
              ) -> None:
    """
    Saves a TSV file.
    
    :param file_name:   Destination 
    :param content:     Content to write, a sequence of rows:
    
                        * Sequence[dataclass] --> Iterate fields
                        * Sequence[Iterable]  --> Iterate iterable
                        
    :param header:      Headers to write:
    
                        * `Sequence[str]` --> A sequence of str
                        * `True` --> get the headers from the dataclass. 
                        * `None` --> no headers.
    """
    if header is True:
        header = dataclasses.asdict( content[0] )
        content = (dataclasses.astuple( x ) for x in content)

    with open( file_name, "w" ) as fout:
        if header is not None:
            fout.write( "\t".join( str( x ) for x in header ) )
            fout.write( "\n" )

        for row in content:
            fout.write( "\t".join( str( x ) for x in row ) )
            fout.write( "\n" )


class _Row:
    __slots__ = "headers", "contents"

    def __init__( self, headers, contents ):
        self.headers = headers
        self.contents = contents

    def items( self ) -> Iterable[Tuple[str, str]]:
        return zip( self.headers, self.contents )

    def __getitem__( self, item ):
        if isinstance( item, str ):
            try:
                item = self.headers[item]
            except KeyError as ex:
                raise KeyError( "The header {} does not exist in the headers {}.".format( repr( item ),
                                                                                          self.headers.keys() ) ) from ex

        return self.contents[item]

    def to_dict( self ):
        return {k: v for k, v in self.items()}


class EDelegate( enum_helper.VagueEnum ):
    """
    What to pass the `klass` used by `load_tsv`.
    
    :cvar ROW:      Pass a `_Row` object: ``(row)``
    :cvar ARGS:     Pass the row as args: ``(*row)``
    :cvar KWARGS:   Pass the row as kwargs (requires `header`): ``(**row)``
    """
    ROW = 0
    ARGS = 1
    KWARGS = 2


def load_tsv( file_name: str,
              header: bool = True,
              klass: Union[Type[T], Callable[..., T]] = _Row,
              factory: object = EDelegate.KWARGS,
              transform = None,
              ) -> Iterable[T]:
    """
    Loads in a TSV file.
    
    :param file_name:   Input 
    :param header:      Takes headers? 
    :param klass:       Transformation applied to individual rows.
                        (Typically a `type`: `dataclass` or `_Row`)
    :param factory:     What to pass to the `klass` initialiser.
                        Ignored if `klass` is `_Row`.
    :param transform:   Transformation applied to individual cells.
    :return:            Iterable of `klass`. 
    """
    if not header and factory == EDelegate.KWARGS:
        raise ValueError( "Cannot use KWARGS if there are no headers." )

    with open_for_read( file_name ) as fin:
        #
        # READ HEADERS
        #
        if header:
            header_map = array_helper.create_index_lookup( tuple( __read_row( fin, transform ) ) )
        else:
            header_map = None

        #
        # TRANSLATE FACTORY
        #
        if klass is _Row or klass is None:
            fac = lambda row: row
        elif factory == EDelegate.ARGS:
            fac = lambda row: klass( *row.contents )
        elif factory == EDelegate.KWARGS:
            fac = lambda row: klass( **row.to_dict() )
        elif factory == EDelegate.ROW:
            fac = klass
        else:
            raise exception_helper.SwitchError( "factory", factory )

        while True:
            try:
                cells = __read_row( fin, transform )
            except StopIteration:
                break

            row = _Row( header_map, cells )
            yield fac( row )


def __read_row( fin, transform ):
    r = next( fin ).rstrip( "\r\n" ).split( "\t" )

    if transform is not None:
        return [transform( x ) for x in r]
    else:
        return r


def sniff_csv( file_name: str ) -> csv.Dialect:
    with open( file_name, "r" ) as fin:
        sample = fin.read( 5000 )
        return cast( csv.Dialect, csv.Sniffer().sniff( sample ) )


# region DEPRECATED

def write_tsv( file_name: str, matrix: Iterable[Iterable[object]] ) -> None:
    warnings.warn( "Deprecated - use save_tsv", DeprecationWarning )
    return save_tsv( file_name, matrix, header = False )

# endregion
