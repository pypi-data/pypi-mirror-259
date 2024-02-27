from typing import Union, Iterable
from mhelper.exception_formatter import EFormat, EOutput, format_traceback_ex, EStyle
from mhelper import array_helper, enum_helper, ansi, exception_helper
import warnings
import sys
from enum import Enum

__all__ = ("install_error_hooks",
           "EHook"
           , "EFormat", "EOutput", "EErrorHook", "EWarningHook") # reexport



_TEnums = Union[EFormat, EOutput, "EErrorHook", "EWarningHook"]


def install_error_hooks( flags: Union["EHook", Iterable[_TEnums], None] = None ) -> None:
    """
    Hooks the system error and warning handlers, using `exception_formatter`
    in their stead.
     
    :param flags:   A member or name of `EHook` or a custom-built sequence
                    containing `EFormat`, `EOutput`, `EErrorHook` and
                    `EWarningHook` members. `EHook.CONSOLE` is the default.
    """
    if flags is None:
        flags = EHook.CONSOLE
    
    if isinstance( flags, str ):
        flags = getattr( EHook, flags.upper() )
        assert isinstance( flags, tuple )

    flags = array_helper.WriteOnceDict( (x.__class__, x) for x in flags )
    formatter_id = enum_helper.rebind( flags[EFormat] )
    output_id = enum_helper.rebind( flags[EOutput] )
    error_hook_id = enum_helper.rebind( flags[EErrorHook] )
    warning_hook_id = enum_helper.rebind( flags[EWarningHook] )

    message_target = __MessageTarget( output_id )

    my_error_hook = __ErrorHook( error_hook_id, formatter_id, message_target )
    my_error_hook.install()

    my_warning_hook = __WarningHook( warning_hook_id, formatter_id, message_target )
    my_warning_hook.install()
    
    
class EErrorHook( Enum ):
    """
    Available error hooks.
    
    :cvar SYSTEM: System
    :cvar IPYTHON: IPython
    """
    SYSTEM = 1
    IPYTHON = 2


class EWarningHook( Enum ):
    """
    Available warning hooks.
    
    :cvar SYSTEM: System
    """
    SYSTEM = 1
    
class EHook:
    """
    Modes of `install_error_hooks`.
    
    :cvar CONSOLE:          Install for console programs.
    :cvar ALT_SCREEN:       Install for ANSI GUIs.
    :cvar JUPYTER:          Install for Jupyter.                    
    """
    CONSOLE = (EFormat.ANSI, EOutput.CONSOLE, EErrorHook.SYSTEM, EWarningHook.SYSTEM)
    ALT_SCREEN = (EFormat.ANSI, EOutput.ALT_SCREEN, EErrorHook.SYSTEM, EWarningHook.SYSTEM)
    JUPYTER = (EFormat.HTML, EOutput.IPYTHON, EErrorHook.IPYTHON, EWarningHook.SYSTEM)




    


# noinspection PyPackageRequirements
class __MessageTarget:
    __slots__ = "flags",

    def __init__( self, flags: EOutput ):
        assert isinstance( flags, EOutput )
        self.flags = flags

    def __call__( self, message: str ):
        if self.flags == EOutput.ALT_SCREEN:
            print( ansi.ALTERNATE_SCREEN_OFF )
            print( message )
            input( "An error has occurred. Press return to continue . . . " )
            print( ansi.ALTERNATE_SCREEN )
        elif self.flags == EOutput.CONSOLE:
            print( message, file = sys.stderr )
        elif self.flags == EOutput.IPYTHON:
            from IPython.core.display import HTML, display
            # noinspection PyTypeChecker
            display( HTML( message ) )
        else:
            raise exception_helper.SwitchError( "EOutput", self.flags )


# noinspection PyPackageRequirements
class __ErrorHook:
    """
    Custom error hook installed by `install_error_hook`.
    """
    __slots__ = "flags", "formatter", "reenterant", "message_target", "original"

    def __init__( self, flags: EErrorHook, formatter: EFormat, message_target ):
        self.flags = flags
        self.reenterant = False
        self.formatter = formatter
        self.message_target = message_target
        self.original = None

    def install( self ):
        if self.flags == EErrorHook.SYSTEM:
            self.original = sys.excepthook
            sys.excepthook = self
        elif self.flags == EErrorHook.IPYTHON:
            # noinspection PyPackageRequirements
            import IPython
            self.original = IPython.InteractiveShell.showtraceback
            IPython.InteractiveShell.showtraceback = self.__my_jupyter_error_hook
            from IPython.core.display import display, HTML
            # noinspection PyTypeChecker
            display( HTML( "The <code>MHelper</code> error hook has been installed." ) )
        else:
            raise exception_helper.SwitchError( "EErrorHook", self.flags )

    def __my_jupyter_error_hook( self, *_, **__ ):
        self( *sys.exc_info() )

    def __call__( self, *a ):
        self.render( *a )

    def render( self, exctype, value, traceback ):
        _ = exctype
        _ = traceback

        if self.reenterant:
            return

        self.reenterant = True
        n = f"{self.__class__.__module__}.{self.__class__.__name__}"

        try:
            data = format_traceback_ex( value,
                                        message = f"`{n}` was notified about an exception.",
                                        style = EStyle.ERROR,
                                        format = self.formatter )
            self.message_target( data )
        except Exception as ex:
            print( f"EX RENDERING EX {ex.__class__.__name__}: {ex}", file = sys.stderr )
            import traceback as traceback_
            print( traceback_.print_tb( ex.__traceback__ ), file = sys.stderr )
        finally:
            self.reenterant = False


class __WarningHook:
    """
    Custom warning hook installed by `install_error_hook`.
    """
    __slots__ = "formatter", "reenterant", "message_target", "flags"

    def __init__( self, flags: EWarningHook, formatter: EFormat, message_target ):
        self.flags = flags
        self.formatter = formatter
        self.reenterant = False
        self.message_target = message_target

    def install( self ):
        if self.flags == EWarningHook.SYSTEM:
            warnings.showwarning = self
        else:
            raise ValueError( "Flags must specify an WARNING_HOOK_." )

    def __call__( self, message, category, filename, lineno, file = None, line = None ):
        if category == FutureWarning:
            return

        if self.reenterant:
            return

        self.reenterant = True
        n = f"{self.__class__.__module__}.{self.__class__.__name__}"

        try:
            data = format_traceback_ex(
                    message,
                    message = f"`{n}` was notified about a warning.\n"
                              f"Category: {category}\n"
                              f"Filename: {filename}\n"
                              f"Line-no: {lineno}\n"
                              f"File: {file}\n"
                              f"Line: {line}",
                    style = EStyle.WARNING,
                    format = self.formatter )
            self.message_target( data )
        finally:
            self.reenterant = False
