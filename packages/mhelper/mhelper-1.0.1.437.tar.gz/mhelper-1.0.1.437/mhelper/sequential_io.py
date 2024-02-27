from typing import Type, Union, Sequence, Optional, IO, TypeVar, Callable
import warnings

from mhelper import exception_helper, file_helper
from mhelper.disposal_helper import IWith
from mhelper.special_types import NOT_PROVIDED


TByteConvertible = Union[Sequence[Union[str, int]], str, int]
T = TypeVar( "T" )
_type = type


class SequentialWriter:
    """
    Converse of `SequentialReader`.
    
    See documentation for `mhelper.io_helper.open2`.
    """
    __slots__ = "file_name", "__file", "__handle", "__gzip"


    def __init__( self, file_name: str, gzip: Optional[bool] = None ):
        self.file_name: str = file_name
        self.__file: Optional[IWith[IO]] = None
        self.__handle: Optional[IO] = None
        self.__gzip = gzip


    def __enter__( self ) -> "SequentialWriter":
        from mhelper.io_helper import open2
        self.__file = open2( self.file_name, write = True, binary = True, gzip = self.__gzip )
        self.__handle = self.__file.__enter__()
        return self


    def __exit__( self, exc_type, exc_val, exc_tb ):
        if self.__file is not None:
            self.__file.__exit__( exc_type, exc_val, exc_tb )
            self.__file = None
            self.__handle = None


    def write_magic( self, magic: TByteConvertible ):
        data = _to_bytes( magic )
        self.__handle.write( data )


    def write_pickle( self, obj: object ):
        import pickle
        pickle.dump( obj, self.__handle, protocol = -1, fix_imports = False )


class SequentialReader:
    """
    Reads values sequentially from a file.
    
    See documentation for `mhelper.io_helper.open2`.
    """
    __slots__ = "file_name", "delete_on_failure", "default", "__file", "__handle", "__failure"


    def __init__( self,
                  file_name: str,
                  default: object = NOT_PROVIDED,
                  delete_on_failure: bool = False,
                  robust: bool = False  # deprecated
                  ):
        """
        :param file_name:           File to read. 
        :param default:             The "reader default" is returned when no
                                    default is provided to an individual method.
                                    See `fail` for more details.  
        :param delete_on_failure:   When set deletes the file and raises a
                                    warning if a read error occurs.
        :param robust:              Deprecated parameter equivalent to 
                                    ``default = None``. 
        """
        if robust:
            default = None

        self.file_name = file_name
        self.delete_on_failure = delete_on_failure
        self.default = default

        self.__file: Optional[IWith[IO]] = None
        self.__handle: Optional[IO] = None
        self.__failure = None


    def __enter__( self ) -> "SequentialReader":
        """
        Entering opens the file.
        Reading is not possible before then.
        """
        try:
            from mhelper.io_helper import open2
            self.__file = open2( self.file_name, binary = True )
            self.__handle = self.__file.__enter__()
        except Exception as ex:
            self.__failure = f"{type( ex ).__name__}: {ex}"
            return self

        self.__failure = None
        return self


    def __exit__( self, exc_type, exc_val, exc_tb ):
        """
        Closes the file.
        
        Deletes the file and raises a warning if in `delete_on_failure` mode.  
        """
        if self.__file:
            self.__file.__exit__( exc_type, exc_val, exc_tb )
            self.__file = None
            self.__handle = None

        if self.__failure and self.delete_on_failure:
            warnings.warn( "\n"
                           "************************************************************\n"
                           "* Failed to load binary file due to an error:              *\n"
                           "************************************************************\n"
                           "* This is probably due to a version incompatibility        *\n"
                           "* You may need to recreate this file.                      *\n"
                           "* The problematic file has been sent to the recycle bin.   *\n"
                           "* If it is important, please retrieve it now.              *\n"
                           "************************************************************\n"
                           "* Error: {}\n"
                           "* File : {}\n"
                           .format( self.__failure, self.file_name ), UserWarning )
            file_helper.recycle_file( self.file_name )


    def read_magic( self, magic: TByteConvertible, default = NOT_PROVIDED ) -> object:
        """
        Reads a magic number.
        (a number that should match an expected value, `magic`).
        
        If the number does *not* the `fail` routine is invoked (see `fail`).
        
        :param magic:   Magic number to expect. 
        :param default: Default value to return. 
        :return:        The magic number or value from `fail`.
        :exception ValueError: Exception from `fail`.
        """
        if self.has_failed:
            return self.fail2()

        data = _to_bytes( magic )
        compare = self.__handle.read( len( data ) )

        if compare != data:
            return self.fail( f"The magic number or version does not match. Expected {data!r} ({magic!r}) got {compare!r}.", default )

        return magic


    @property
    def has_failed( self ) -> bool:
        """
        Returns if the `__failure` flag has been set.
        """
        return self.__failure is not None


    def fail2( self, default : Union[T, object] = NOT_PROVIDED ) -> Union[T, object]:
        """
        Handles the case where a value cannot be obtained due to a previous
        failure. See `fail` for more details.
        
        :param default: Default value to return. 
        :return:        Either the `default` or `self.default`.
        :exception ValueError: No `default` or `self.default` provided.
        """
        assert self.has_failed

        if default is not NOT_PROVIDED:
            return default

        if self.default is not NOT_PROVIDED:
            return self.default

        raise ValueError( f"Cannot read due to a previous read failure and no default value was provided.\nPrevious failure:\n{self.__failure}" )


    def fail( self, message: str, default : T = NOT_PROVIDED, exception = None ):
        """
        Handles the case where a value cannot be obtained.
        
        * If a `default` is provided, it is returned.
        * If a `self.default` is provided, it is returned.
        * A `ValueError` is raised.
        
        Regardless of what happens, the `__failure` flag is set, which causes
        all further attempts at reading to also fail. This means that
        invocations such as `read_magic`, `read_pickle` will only read the
        pickle data should the magic number be valid (assuming we have provided
        a default so as not to cause an error). 
        
        :param message:     Description of failure, used only if raising an 
                            exception.  
        :param default:     Default value to return. 
        :param exception:   Causative exception to raise from (if present),
                            used only if raising an exception.  
        :return:            Either the `default` or `self.default`.
        :exception ValueError: No `default` or `self.default` provided. 
        """
        self.__failure = message

        if default is not NOT_PROVIDED:
            return default

        if self.default is not NOT_PROVIDED:
            return None

        raise ValueError( message ) from exception


    def read_pickle( self,
                     type: Type[T],
                     default: object = NOT_PROVIDED,
                     assertion: Callable = None,
                     ) -> T:
        """
        Reads pickle data.
        
        :param type:        Expected data type.
                            If this is a mismatch then `fail` is invoked. 
        :param default:     Value used by `fail`. 
        :param assertion:   Any other assertion on the return value.
                            If this fails then `fail` is invoked.
        :return:            Result or value from `fail`.
        :exception ValueError: From `fail`. 
        """
        if self.has_failed:
            return self.fail2( default )

        import pickle

        try:
            data = pickle.load( self.__handle, fix_imports = False )
        except Exception as ex:
            return self.fail( f"Error loading file due to the error: {_type( ex ).__name__}: {ex}", default, ex )

        if type is not None:
            if not isinstance( data, type ):
                return self.fail( f"Deserialised object from file «{self.file_name}» was expected to be of type «{type}» but it's not, its of type «{_type( data )}» with a value of «{data}».", default )

        if assertion is not None:
            if not assertion( data ):
                return self.fail( f"Deserialised object from file «{self.file_name}» was expected to be of match assertion «{assertion}» but it does not. The result is of type «{_type( data )}» with a value of «{data}».", default )

        return data


def _to_bytes( obj: TByteConvertible ):
    if isinstance( obj, tuple ) or isinstance( obj, list ):
        return b"".join( _to_bytes( obj2 ) for obj2 in obj )

    if isinstance( obj, str ):
        data = obj.encode()
    elif isinstance( obj, int ):
        data = obj.to_bytes( 4, "little" )
    else:
        raise exception_helper.type_error( "obj", obj, [str, int] )

    return data
