"""
DEPRECATED MODULE
"""
# !EXPORT_TO_README
import os
import sys
import warnings
from typing import Union
from mhelper import ansi





def print_traceback( ex = None, **kwargs ) -> None:
    """
    `print`\s the result of `format_traceback_ex` to stderr. 
    """
    warnings.warn( "Deprecated - use exception_formatter", DeprecationWarning )
    msg = format_traceback_ex( ex, **kwargs )
    print( msg, file = sys.stderr )


def get_ansi_support() -> bool:
    """
    Gets the level of ANSI support.
    
    .. note::
        
        There is no real way to determine if the current terminal supports
        ANSI codes, so we do unless explicitly told otherwise.
    """
    warnings.warn("Deprecated.", DeprecationWarning)
    if os.getenv( "NO_ANSI" ):
        return False
    
    return True


def install_error_hook( ):
    """
    Adds `print_traceback` to the system exception hook.
    """
    warnings.warn("Deprecated - use exception_formatter", DeprecationWarning)
    from mhelper.exception_hooks import install_error_hooks, EHook
    install_error_hooks( EHook.CONSOLE )


def format_traceback_ex( exception: Union[BaseException, str] = None,
                         *,
                         wordwrap: int = 0,
                         warning: bool = False,
                         style: str = None,
                         message: str = None,
                         formatter = "ANSI" ) -> str:
    """
    Pretty formats a traceback using ANSI escape codes.
    
    :param exception:       Exception to print the traceback for. 
    :param wordwrap:        Length of wrapping for lines. 0 assumes a default.
    :param style:           Error style ("information", "warning", "error" or the first letter thereof) 
    :param warning:         Deprecated. Use `style`. 
    :param message:         Optional message to include at the end of the traceback. 
    :return: The formatted traceback, as a `str`.
    """
    warnings.warn("Deprecated - use exception_formatter", DeprecationWarning)
    
    if style is None:
        style = "w" if warning else "e"
    
    if style == "w":
        style = "WARNING"
    elif style == "e":
        style = "ERROR"
    
    from mhelper.exception_formatter import format_traceback_ex
    
    return format_traceback_ex( exception, message, style, formatter )





def highlight_filename( fn ):
    a, b = os.path.split( fn )
    return a + os.path.sep + ansi.BOLD + b + ansi.RESET


def qformat( text: str, map: dict = None ) -> str:
    """
    Quick format, accepts HTML-like codes::
    
        This text is <B>bold</B>.
    
    :param text:    Text to parse
    :param map:     Code map - HTML keys to tuples of on codes and off codes.
                    The default map   
    :return: 
    """
    if map is None:
        map = {
            "I": (ansi.ITALIC, ansi.ITALIC_OFF),
            "B": (ansi.BOLD, ansi.BOLD_OFF),
            "U": (ansi.UNDERLINE, ansi.UNDERLINE_OFF),
            "D": (ansi.DIM, ansi.DIM_OFF),
            "V": (ansi.INVERSE, ansi.INVERSE_OFF),
            "S": (ansi.STRIKETHROUGH, ansi.STRIKETHROUGH_OFF),
            }
    
    for key, (on_code, off_code) in map.items():
        text = text.replace( f"<{key}>", on_code )
        text = text.replace( f"</{key}>", off_code )
    
    return text
