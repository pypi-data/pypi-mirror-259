"""
Contains various assertion functions, generic exception classes and functions
to generate errors which actually try to provide helpful messages.

Notable examples include `SwitchError`, `NotSupportedError` and `safe_cast`.

This package also includes functions for more easily parsing exception
tracebacks. 
"""
# !EXPORT_TO_README
import inspect
import subprocess
import sys
import warnings
from inspect import FrameInfo
from typing import cast, Collection, Iterable, List, Optional, Set, Tuple, Type, TypeVar, Union, get_args, get_origin

from mhelper.special_types import NOT_PROVIDED  # Reexport also


TType = Union[Type, Iterable[Type]]
"""A type, or a collection of types"""

T = TypeVar( "T" )


class NotSupportedError( Exception ):
    """
    Since `NotImplementedError` looks like an abstract-base-class error to the
    IDE, `NotSupportedError` provides a more explicit alternative.
    """
    __slots__ = ()
    
    
    def __init__( self, klass = None, method = None ):
        """
        :param klass:       Class *or* message. 
        :param method:      Method - auto-generates a message. 
        """
        if method is None:
            if klass is None:
                super().__init__()
            else:
                super().__init__( klass )
        else:
            super().__init__( f"The method '{method.__name__}' is not supported for this type '{klass.__name__}'." )


class LogicError( RuntimeError ):
    """
    Signifies a logical error in the subroutine which generally isn't the
    caller's fault.
    """
    __slots__ = ()


ImplementationError = LogicError
"""Alias for LogicError"""


class MultipleError( Exception ):
    """
    More than one result was found.
    """
    __slots__ = ()


class NotFoundError( Exception ):
    """
    Like `FileNotFound` error, but when applied to something other than files.
    """
    __slots__ = ()


class ExistsError( Exception ):
    """
    Like `FileExistsError`, but when applied to something other than files.
    """
    __slots__ = ()


class ParameterError( Exception ):
    """
    Like `ValueError`, but describes the offending parameter.
    """
    __slots__ = ()
    
    
    def __init__( self, name, value = None ):
        super().__init__( "The parameter «{}» requires a value that is not «{}».".format( name, value ) )


class SwitchError( Exception ):
    """
    An error selecting the case of a switch.
    """
    __slots__ = ()
    
    
    def __init__( self, name: str, value: object, *, instance: bool = False, details: Optional[str] = None ):
        """
        CONSTRUCTOR
        
        :param name:        Name of the switch 
        :param value:       Value passed to the switch 
        :param instance:    Set to indicate the switch is on the type of value (`type(value)`)
        :param details:     Additional message to append to the error text. 
        """
        if details is None:
            details = ""
        else:
            details = " Further details: {}".format( details )
        
        if instance:
            super().__init__( "The switch on the type of «{}» does not recognise the value «{}» of type «{}».{}".format( name, value, type( value ), details ) )
        else:
            super().__init__( "The switch on «{}» does not recognise the value «{}» of type «{}».{}".format( name, value, type( value ), details ) )


class SubprocessError( Exception ):
    """
    Raised when the result of calling a subprocess indicates an error.
    """
    __slots__ = ()
    
    
    def __init__( self, message, return_code ):
        super().__init__( message )
        self.return_code = return_code


def add_details( exception: Exception, **kwargs ) -> None:
    """
    Attaches arbitrary information to an exception.
    
    :param exception:   Exception 
    :param kwargs:      Information to attach
    """
    args = list( exception.args )
    
    message = create_details_message( **kwargs )
    
    if len( args ) > 0 and isinstance( args[0], str ):
        args[0] += message
    else:
        args.append( message )
    
    exception.args = tuple( args )


def create_details_message( **kwargs ):
    from mhelper import string_helper
    
    result = [""]
    
    lk = 1
    lt = 1
    
    for k, v in kwargs.items():
        lk = max( len( str( k ) ), lk )
        lt = max( len( string_helper.type_name( v ) ), lt )
    
    for k, v in kwargs.items():
        result.append( "--> {0} ({1}) = «{2}»".format( str( k ).ljust( lk ), string_helper.type_name( v ).ljust( lt ), v ) )
    
    return "\n".join( result )


def abs_cast( *args, **kwargs ) -> T:
    """
    Variant of `safe_cast` which enforces the `absolute` parameter.
    """
    return safe_cast( *args, absolute = True, **kwargs )


def safe_cast_iter( name: str, values: Iterable[T], type_: Type[T], *args, **kwargs ) -> Iterable[T]:
    for index, item in enumerate( values ):
        safe_cast( f"{name}[{index}]", item, type_, *args, **kwargs )
    
    return values


class _SafeCaster:
    __slots__ = "types",
    
    
    def __init__( self, types: TType ):
        self.types = types
    
    
    def __call__( self, value: object, name: str = "safe_cast.value", **kwargs ):
        return safe_cast( name, value, self.types, **kwargs )


class _SafeCast:
    def __getitem__( self, types: TType ):
        """
        Alternative syntax:
        
        safe_cast[types]( value, **kwargs )
        """
        return _SafeCaster( types )
    
    
    def __repr__( self ):
        return f"{type( self ).__name__}"
    
    
    def __call__( self,
                  name: str,
                  value: object,
                  types: TType,
                  *,
                  info: str = None,
                  err_class: Type[Exception] = TypeError,
                  absolute = False
                  ) -> T:
        """
        Asserts that the value is of the specified type.
        
        :param name:            Name of the value 
        :param value:           The value itself 
        :param types:           The type the value must be.
                                This can be a list or tuple, in which case any of these types is accepted.
                                This can also be a `Union` of types. 
        :param info:            Additional information to append to the error message. 
        :param err_class:       Type of error to raise should an exception occur. 
        :param absolute:        When `True`, the `value` must be the specified `type_`, not just inherited from. 
        :return: 
        """
        types_it: Iterable[type]
        type__: Optional[type]
        
        if get_origin( types ) == Union:
            types_it = get_args( types )
        elif not isinstance( types, list ) and not isinstance( types, tuple ):
            types_it = cast( Iterable[type], (types,) )
        else:
            types_it = types
        
        if absolute:
            for type__ in types_it:
                if type( value ) == type__ if type__ is not None else value is None:
                    return cast( T, value )
        else:
            for type__ in types_it:
                if isinstance( value, type__ ) if type__ is not None else value is None:
                    return cast( T, value )
        
        if info is not None:
            info = " Extra information = {}".format( info )
        else:
            info = ""
        
        raise type_error( name, value, types, err_class, info, "SAFE CAST FAILED" )  # safe_cast error raise  


safe_cast = assert_type = _SafeCast()


def coerce_cast( name, value, type ):
    if isinstance( value, type ):
        return value
    
    try:
        return type( value )
    except Exception as ex:
        raise type_error( name, value, type,
                          info = "I tried to coerce the value to the required type using the constructor, "
                                 "but either the value is invalid or the constructor doesn't support conversion from this type. "
                                 "See the inner exception for details.",
                          title = "COERCE CAST FAILED" ) from ex


def default( *args, ex: Optional[Exception] = None, exc: Type[BaseException] = ValueError, placeholder = NOT_PROVIDED ):
    """
    Returns the first non-placeholder value, or raises an error.
    
    :param args:        One or more values
    :param ex:          Exception to raise from (optional) 
    :param exc:         Exception class
    :param placeholder: Value to expect as the placeholder.
                        `NOT_PROVIDED` by default.
    """
    for arg in args:
        if arg is not placeholder:
            return arg
    
    raise exc( "The value could not be obtained and no default has been provided. "
               f"This error has been detected by {__name__}.{default.__qualname__}. "
               "Please look at the call stack to identify the missing value." ) from ex


default_or_fail = default


def exception_to_string( ex: BaseException ):
    result = []
    
    ex_re: Optional[BaseException] = ex
    
    while ex_re:
        result.append( str( ex_re ) )
        ex_re = ex_re.__cause__
    
    return "\n---CAUSED BY---\n".join( result )


def run_subprocess( command: str ) -> None:
    """
    Runs a subprocess, raising `SubprocessError` if the error code is set.
    """
    status = subprocess.call( command, shell = True )
    
    if status:
        raise SubprocessError(
                "SubprocessError 1. The command «{}» exited with error code «{}». If available, checking the console output may provide more details."
                    .format( command, status ), return_code = status )


def format_types( type_: TType ) -> str:
    warnings.warn( "Deprecated - use format_type.", DeprecationWarning )
    return format_type( type_ )


def format_type( type_ ):
    if isinstance( type_, list ) or isinstance( type_, tuple ):
        from mhelper import string_helper
        return string_helper.array_to_string( type_, delimiter = ", ", last_delimiter = " or ", format = format_type )
    elif hasattr( type_, "__qualname__" ):
        return type_.__qualname__
    else:
        return str( type_ )


def assert_instance( name: str, value: object, type_: TType ) -> None:
    if isinstance( type_, type ):
        type_ = (type_,)
    
    if not any( isinstance( value, x ) for x in type_ ):
        raise TypeError( instance_message( name, value, type_, "ASSERT INSTANCE FAILED" ) )


def assert_type_or_none( name: str, value: Optional[T], type_: Union[Type[T], Iterable[Type[T]]] ) -> T:
    if value is None:
        return cast( T, value )
    
    return safe_cast( name, value, type_ )


def instance_message( name: str, value: object, type_: TType = None, info: str = None, title: str = None ) -> str:
    """
    Creates a suitable message describing a type error.
    
    :param name:        Name 
    :param value:       Value 
    :param type_:       Expected type 
    :param info:        Extra information text (at end of message).
    :param title:       Extra information text (at start of message).
    :return:            The message
    """
    from mhelper import string_helper
    value_str = string_helper.max_width( repr( value ), 5000 )
    
    ta = type( value )
    
    exf = format_type( type_ )
    exa = format_type( ta )
    
    if exf == exa:
        exf += f" (ID:{id( type_ ):X})"
        exa += f" (ID:{id( ta ):X})"
    
    if ta is type_:
        exa += " (warning: this is the same type instance as the expected, is this exception erroneous?)"
    
    r = [
        f"{title}\n" if title else None,
        f"* The type of the value is incorrect.\n",
        f"  *    Value name: {name!r}\n",
        f"  * Expected type: {exf}\n" if type_ is not None else None,
        f"  * Received type: {exa}\n",
        f"  *         value: {value_str}",
        f"\n* {info}" if info else None
        ]
    return "".join( x for x in r if x )


TException = TypeVar( "TException", bound = Exception )


def type_error( name: str,
                value: object,
                type_: TType = None,
                err_class: Type[TException] = TypeError,
                info: str = None,
                title: str = None,
                ) -> TException:
    """
    Returns an exception documenting a type-error.

    See `instance_message` for parameter details.
    """
    return err_class( instance_message( name, value, type_, info, title ) )


class SimpleTypeError( TypeError ):
    __slots__ = ()
    
    
    def __init__( self, name: str, value: object, types: TType ):
        super().__init__( instance_message( name, value, types ) )


class LoopDetector:
    """
    Detects infinite loops and manages looping.
    
    Usage
    -----
    
    A normal `while` loop.
    We loop until `spam` is `False`, calling `safe` each iteration.
    
        ```
        safe = LoopDetector( 100 )
        while spam:
            safe()
            ...
        ```
    
    * * * *
    
    Another normal while loop. 
    This time we pass `spam` through `safe` for brevity.
     
        ```
        safe = LoopDetector( 100 )
        while safe( spam ):
            ...
        ```
        
    * * * *
    
    List comprehension.
    We pass our elements through `safe` to ensure our iterator is finite.
    
        ```
        safe = LoopDetector( 100 )
        y = [ safe( x ) for x in z ]
        ```
        
    * * *
    
    Exit-able iterator.
    By using `safe` to encapsulate the loop, we can call `.exit()` to exit the loop.
    This differs from `break` in that we can exit deeper loops.
    
        ```
        safe = LoopDetector( 100 )
        while safe():
            if not spam:
                safe.exit()
        ```
            
    * * *
    
    Persistent iterator.
    This is the converse of the above, only by calling `persist` does the loop continue.
    
        ```
        safe = LoopDetector( 100, invert = True )
        while safe():
            if spam:
                safe.persist()
        ```
    """
    __slots__ = ("__limit", "__current", "__info", "__invert", "check")
    
    
    def __init__( self, limit, info = None, *, invert = False ):
        """
        CONSTRUCTOR
        :param limit:   Limit for loops.
                        This should be set to a value in line with the task. 
        :param info:    Useful information to be displayed should a loop occur.
                        Should have a useful `__str__` representation. 
        :param invert:  When `True`, a `persist` call is required to continue
                        the loop.
        """
        self.__limit = limit
        self.__current = 0
        self.__info = info
        self.__invert = invert
        self.check = True
    
    
    def reset( self ):
        """
        Resets the safety counter, allowing this detector to be used again.
        """
        self.__current = 0
    
    
    def persist( self ):
        """
        Sets the continuation parameter to True (keep looping) 
        """
        self.check = True
    
    
    def exit( self ):
        """
        Sets the continuation parameter to False (stop looping) 
        """
        self.check = False
    
    
    def __call__( self, pass_through = NOT_PROVIDED ):
        """
        Increments the counter, causing an error if the counter hits the limit.
        
        This call returns the continuation parameter, :ivar:`check`, which is
        controlled through :func:`keep`, :func:`exit` and :ivar:`__invert`.
        This allows the loop detector to be used as a predicate on loop continuation.
        
        Alternatively, a `pass_through` parameter may be provided, which is returned in lieu
        of the continuation parameter, and allows this function to be called as part
        of a lambda expression or list comprehension.
        """
        self.__current += 1
        
        if self.__current >= self.__limit:
            raise ValueError( "Possible infinite loop detected. Current loop count is {}. If this detection is in error a higher `limit` should be specified, otherwise the infinite loop should be fixed. Further information: {}".format( self.__current, self.__info ) )
        
        if pass_through is NOT_PROVIDED:
            r = self.check
        else:
            r = pass_through
        
        if self.__invert:
            self.check = False
        
        return r


class Object:
    pass


def get_traceback_ex( ex: BaseException = None ):
    warnings.warn( "Deprecated - use exception_formatter", DeprecationWarning )
    from mhelper import exception_formatter
    return exception_formatter.get_traceback_ex( ex )


def assert_environment():
    from mhelper import file_helper, module_helper, string_helper
    
    #
    # Python version
    #
    module_helper.assert_version()
    
    #
    # Working directory
    #
    file_helper.assert_working_directory()
    
    #
    # UTF-8
    #
    string_helper.assert_unicode()
    file_helper.assert_working_directory()


def assert_provided( value, details ):
    if value is NOT_PROVIDED:
        raise ValueError( "Failed to get item. {}".format( details ) )
    
    return value


class FireOnce:
    __slots__ = "added",
    
    
    def __init__( self ):
        self.added: Set[tuple] = set()
    
    
    def __call__( self, *t ):
        if t in self.added:
            raise ValueError( "FireOnce has checked on a duplicate value:\n{}".format( "\n".join( "* VALUE #{}\n    * {}".format( i, x ) for i, x in enumerate( t ) ) ) )
        
        self.added.add( t )


def catch( fn, default = None, ex_type = Exception ):
    """
    Converts an exception to a return value.
    
    :param fn:          Function to execute 
    :param default:     Return value should the function raise an exception 
    :param ex_type:     Exception type to catch      
    :return:            `fn` return value or `default` if the function raises `ex_type`. 
    """
    try:
        return fn()
    except ex_type:
        return default


def assert_sets_equal( a: Collection[T], b: Collection[T] ) -> None:
    """
    Checks the sets are the same, providing a useful error message if not.
        
    :exception ValueError:  Sets are not the same, or the inputs contain duplicates.  
    """
    provided = frozenset( a )
    required = frozenset( b )
    
    if len( provided ) != len( a ):
        raise ValueError( "Duplicate provided values." )
    
    if len( required ) != len( b ):
        raise ValueError( "Duplicate required values." )
    
    extra = provided - required
    missing = required - provided
    
    if missing:
        raise ValueError( "Required value(s) not provided: {}" )
    
    if extra:
        raise ValueError( "Value(s) provided that were not required: {}" )


# region Deprecated

# noinspection PyDeprecation
def get_traceback( ex: BaseException = None ) -> str:
    """
    DEPRECATED
    """
    warnings.warn( "obsolete - use `get_traceback_collection`", DeprecationWarning )
    r = []
    
    if ex is None:
        ex = sys.exc_info()[1]
    
    causes: List[Tuple[int, BaseException]] = []
    
    while ex is not None:
        causes.append( (len( causes ), ex) )
        ex = ex.__cause__
    
    for i, ex in causes:
        r.append( __format_traceback( ex.__traceback__, "{}/{}: {}".format( len( causes ) - i - 1, len( causes ), type( ex ).__name__ ), len( causes ) - i ) )
    
    r.append( "Notice: get_traceback is obsolete - please use get_traceback_ex" )
    
    return "\n".join( r )


# noinspection PyDeprecation
def __format_traceback( tb, title, prefix ):
    """
    DEPRECATED
    """
    warnings.warn( "obsolete - use `get_traceback_collection`", DeprecationWarning )
    r = []
    
    # The "File "{}", line {}" bit can't change because that's what PyCharm uses to provide clickable hyperlinks.
    
    r.append( "*{} traceback:".format( title ) )
    for index, frame in reversed( list( enumerate( inspect.getouterframes( tb.tb_frame )[1:] ) ) ):
        __add_fmt_traceback( frame, -1 - index, prefix, r )
    
    for index, frame in enumerate( inspect.getinnerframes( tb ) ):
        __add_fmt_traceback( frame, index, prefix, r )
    
    return "\n".join( r )


# noinspection PyDeprecation
def __add_fmt_traceback( frame: FrameInfo, index, prefix, r ):
    """
    DEPRECATED
    """
    warnings.warn( "obsolete - use `get_traceback_collection`", DeprecationWarning )
    r.append( '{}.{}. File "{}", line {}; Function: {}'.format( prefix, index, frame.filename, frame.lineno, frame.function ) )
    if frame.code_context:
        r.append( "\n".join( frame.code_context ) )
    
    locals = frame.frame.f_locals
    
    if locals:
        from mhelper import string_helper
        for i, (k, v) in enumerate( locals.items() ):
            if i > 10:
                r.append( "          Local: {} more locals not shown".format( len( locals ) - 10 ) )
                break
            
            try:
                repr_v = repr( v )
            except Exception:
                repr_v = "(repr_failed)"
            
            r.append( "          Local: {}={}".format( k, string_helper.max_width( repr_v, 80 ) ) )

# endregion
