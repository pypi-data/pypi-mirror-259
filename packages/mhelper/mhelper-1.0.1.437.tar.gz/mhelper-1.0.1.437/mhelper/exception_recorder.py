import sys
import functools
import os
from dataclasses import dataclass
from typing import List, Optional, Callable, Set
from mhelper.exception_formatter import EStyle, format_traceback as _format_traceback, EFormat as _EFormat
from mhelper import string_helper

_DEFAULT = object()

__all__ = ("print_traceback",
           "emulate_traceback",
           "try_get_log_ref",
           "PrintTracebackResult",
           "ExceptionInfo",
           "ErrorRecorder",
           "DirectoryErrorRecorder",
           "ConsoleErrorRecorder",
           "targets",
           "EStyle")  # reexport


def print_traceback( exception: Optional[BaseException],
                     message: str = "",
                     ref: bool = False,
                     is_verbose: bool = False,
                     target: Callable[[str], None] = _DEFAULT,
                     style: EStyle = EStyle.ERROR,
                     condition: bool = True,
                     ) -> "PrintTracebackResult":
    """
    Sends the traceback to the registered console (and optionally, log) handlers.
     
    :param condition:       If `False`, no output is produced.
                            
    :param style:           Message style.
    
    :param exception:       Exception to write
     
    :param message:         Reason message.
    
                            A short description of why the error has been caught or is being
                            printed. May be blank.
                             
    :param ref:             Write error to `Targets.log`.
    
                            If this is `True` a unique ID is generated for the error and the message
                            is *also* sent to `Targets.log`.
                            
                            The unique ID is returned in the result (e.g. to display on a web page).
                            
                            The `exception_formatter` module may be executed to retrieve these
                            errors.
                            
                            Note that `Targets.log` requires setup before use. See `Targets`.
                              
    :param is_verbose:      Similar to `condition`, however if the environment variable
                            `MJR_EXTRA_DEBUG` has been set then the message *is* printed.
                            
    :param target:          Print target.
    
                            By default this is `Targets.console`.
                            However, this may be set to a `None`, an `ErrorRecorder` or a method
                            capable of receiving a string in lieu of this.
                              
    :return:                A `PrintTracebackResult` object containing the reference used, if any. 
    """
    #
    # Condition switch
    #
    if not condition:
        return PrintTracebackResult( "[NOT-RECORDED]", None )

    #
    # Verbosity switch
    #
    if is_verbose:
        ENV_VAR_NAME = "MJR_EXTRA_DEBUG"
        if not os.environ.get( ENV_VAR_NAME ):
            return PrintTracebackResult( "[NO-LOG]", None )

        message += f"Normally this trace wouldn't appear, but `{ENV_VAR_NAME}` is set."

    #
    # Generate reference number
    #
    if ref is True:
        ref_str = string_helper.get_random_text( "AA11AA" )
    elif ref:
        ref_str = ref
    else:
        ref_str = None

    if ref_str:
        log_ref = f"[LOG-REF: {ref_str}]"
        message += log_ref
    else:
        log_ref = "[NOT-REFERENCED]"

    #
    # Send to console target
    #
    info = ExceptionInfo( exception, message, ref_str, style )

    if target is None:
        pass
    elif target is _DEFAULT:
        targets.console.record_error( info )
    elif isinstance( target, ErrorRecorder ):
        target.record_error( info )
    else:
        ConsoleErrorRecorder( target ).record_error( info )

    #
    # Send to recorder target
    #
    if ref_str:
        targets.log.record_error( info )

        # Try to store the ref on the exception itself
        try:
            setattr( exception, "exception_formatter_ref", log_ref )
        except Exception:
            pass

    #
    # Return information
    #
    return PrintTracebackResult( log_ref, ref_str )


def emulate_traceback( exception, *args, **kwargs ):
    try:
        raise exception
    except Exception as ex:
        return print_traceback( ex, *args, **kwargs )


def try_get_log_ref( exception: object ) -> str:
    return getattr( exception, "exception_formatter_ref", "[NO-REFERENCE]" )


@dataclass
class PrintTracebackResult:
    """
    :cvar ref:  Log reference, if requested, otherwise a message informing the
                user than no reference is available.
                
                `ref` is suitable for inserting into a user-friendly message and
                will contain descriptive text as opposed the a bare ID.
    :cvar bare_ref: The bare reference ID, with no descriptive text. `None` if
                    no reference was generated. 
    """
    ref: str
    bare_ref: Optional[str]


@dataclass
class ExceptionInfo:
    """
    Information about an exception, sent to an `ErrorRecorder`.
    """
    exception: Optional[BaseException]
    message: str
    ref: Optional[str]
    style: EStyle


class ErrorRecorder:
    """
    Class capable of handling errors.
    """

    def record_error( self, info: ExceptionInfo ):
        raise NotImplementedError( "abstract" )


class DirectoryErrorRecorder( ErrorRecorder ):
    """
    Sends the error to a file inside a folder.
    Requires a valid reference.
    """

    def __init__( self, directory: str ):
        self.directory = directory
        os.makedirs( directory, exist_ok = True )

    def record_error( self, info: ExceptionInfo ):
        message_ansi = _format_traceback( info.exception,
                                          message = info.message,
                                          style = info.style,
                                          format = _EFormat.ANSI )

        from mhelper import io_helper
        file_name_ansi = os.path.join( self.directory, info.ref + ".ansi" )
        message_ansi = f"{sys.executable} {sys.argv}\n{message_ansi}"
        io_helper.write_all_text( file_name_ansi, message_ansi )


class ConsoleErrorRecorder( ErrorRecorder ):
    """
    Sends the error to a function (stderr by default).
    """

    def __init__( self, target: Callable[[str], None] = functools.partial( print, file = sys.stderr ) ):
        self.target = target

    def record_error( self, info: ExceptionInfo ):
        message_ansi = _format_traceback( info.exception,
                                          message = info.message,
                                          style = info.style,
                                          format = _EFormat.ANSI )

        self.target( message_ansi )


class _BadTarget( ErrorRecorder ):
    """
    Generates an error message it tries to record an error.
    """

    def record_error( self, info: ExceptionInfo ):
        raise RuntimeError( "Cannot record this error because no target has been set." )


class _TargetsType:
    """
    The targets to send errors to.
    These may be changed.
    
    :ivar console:  Errors are always sent here, unless it is expliclity requested that they are not.
    :ivar log:      Errors with reference IDs are also sent here.
                    This is `_BadTarget` by default and must be configured before use.
                    (Presumably by setting this to a `DirectoryErrorRecorder`). 
    """
    __slots__ = ("console", "log")

    def __init__( self ):
        self.console: ErrorRecorder = ConsoleErrorRecorder()
        self.log: ErrorRecorder = _BadTarget()


targets = _TargetsType()

if __name__ == "__main__":
    from mhelper import exception_recorder_exe

    exit( exception_recorder_exe._main() )
