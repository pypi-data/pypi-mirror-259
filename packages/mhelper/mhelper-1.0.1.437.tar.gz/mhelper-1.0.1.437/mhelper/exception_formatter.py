"""
Prints pretty error tracebacks with full stack and variables display.
"""

import inspect
import itertools
import os
import sys
import warnings
from builtins import Exception
from dataclasses import dataclass
from enum import Enum
from inspect import FrameInfo
from typing import Callable, Iterable, List, Optional, Tuple, Type, TypeVar, Union

from mhelper import ansi, string_helper, array_helper, enum_helper, exception_helper

__all__ = (
    "format_traceback_ex",
    "get_traceback_ex",
    "EFormat",
    "EStyle",
    "ELocalOrigin",
    "EOutput"
)

_T = TypeVar( "_T" )


class _EFrameOrigin( Enum ):
    """
    Inferred origin of the frame's file. 
    """
    USER = 1
    SITE = 2
    SYSTEM = 3


class ELocalOrigin( Enum ):
    """
    Inferred origin of a local variable.
    """
    NORMAL = 1
    VERBOSE = 2


class EStyle( Enum ):
    """
    Style of error message.
    """
    ERROR = 1
    WARNING = 2
    INFORMATION = 3


class EFormat( Enum ):
    """
    Format of error message.
    """
    ANSI = 1
    TEXT = 2
    HTML = 3


class EOutput( Enum ):
    """
    Output destinations for error hooks.
    
    :cvar CONSOLE:      Stderr
    :cvar ALT_SCREEN:   Stderr, switching from and restoring alt-screen
    :cvar IPYTHON:      IPython HTML display
    """
    CONSOLE = 1
    ALT_SCREEN = 2
    IPYTHON = 3






class TracebackCollection:
    """
    Collection of exceptions, as `TbEx` objects.
    
    :ivar exceptions: Exceptions, in order of cause, each exception is caused by
                      the previous. So the ultimate cause is the end and the
                      receiver is at the start.
    """
    __slots__ = "exceptions",

    def __init__( self ):
        self.exceptions: List[_TbEx] = []


class _TbEx:
    """
    Describes an `Exception` in a format accessible for printing the output.
    
    :ivar frames:       Call stack as `TbFrame` objects.
    :ivar collection:   Owning `TbCollection`.
    :ivar index:        Index of this exception in the cause chain.
    :ivar exception:    Exception itself.
    :ivar type:         Type name of the exception
    :ivar message:      String representation of the exception
    :ivar is_first:     Is this the ultimate exception in the chain.
    :ivar is_cause:     Is this a cause of the ultimate exception.
    """
    __slots__ = "frames", "collection", "index", "exception", "type", "message", "is_first", "is_cause"

    def __init__( self, col: TracebackCollection, index, ex ):
        self.frames: List[_TbFrame] = []
        self.collection = col
        self.index = index
        self.exception = ex
        self.type = type( ex ).__name__
        self.message = str( ex )
        self.is_first = self.index == 0
        self.is_cause = self.index != 0


class _TbFrame:
    """
    Describes a `FrameInfo` in a format accessible for printing the output.
    
    :ivar exception:    Owning `TbEx`
    :ivar index:        Index of frame.
    :ivar file_name:    Filename
    :ivar line_no:      Line number
    :ivar function:     Function name
    :ivar code_context: Code context
    :ivar locals:       Locals
    :ivar origin:       Hints on origin (see `_EFrameOrigin`)
    """
    __slots__ = "exception", "index", "file_name", "line_no", "function", "next_function", "code_context", "locals", "origin"

    def __init__( self, ex: _TbEx, index: int, frame: FrameInfo ):
        self.exception: _TbEx = ex
        self.index: int = index
        self.file_name: str = frame.filename
        self.line_no: int = frame.lineno
        self.function: str = frame.function
        self.next_function: str = ""
        self.code_context: str = "\n".join( frame.code_context ).strip() if frame.code_context else ""
        self.locals: List[_TbLocal] = []
        fn = self.file_name.replace( os.path.sep, "/" )
        self.origin = _EFrameOrigin.SYSTEM if _TbFrame.__is_core_package(
                fn ) else _EFrameOrigin.SITE if _TbFrame.__is_site_package( fn ) else _EFrameOrigin.USER

    @staticmethod
    def __is_site_package( fn ) -> bool:
        return _TbFrame.__is_in( fn, "/site-packages/", "/lib/" )

    @staticmethod
    def __is_core_package( fn ) -> bool:
        # noinspection SpellCheckingInspection
        return _TbFrame.__is_in( fn,
                                 "/lib/runpy.py",
                                 "/lib/asyncio/",
                                 "/site-packages/ipywidgets/",
                                 "/site-packages/traitlets/",
                                 "/site-packages/tornado/",
                                 "/site-packages/ipykernel/",
                                 "/site-packages/IPython/",
                                 "site-packages/ipykernel_launcher.py"
                                 )

    @staticmethod
    def __is_in( fn, *args ):
        for arg in args:
            if arg in fn:
                return True

        return False


class _TbLocal:
    """
    Describes a local variable.
    
    :ivar frame:    Frame
    :ivar index:    Index of local
    :ivar name:     Name of local
    :ivar value:    Value of local
    :ivar repr:     String representation of local (truncated to a reasonable length)
    :ivar origin:   Hints on origin (see `ELocalOrigin`)
    """
    __slots__ = "frame", "index", "name", "value", "repr", "origin"

    def __init__( self, fr: _TbFrame, index: int, key: str, value: object, rep: str ):
        self.frame = fr
        self.index = index
        self.name = key
        self.value = value
        self.repr = rep
        self.origin = ELocalOrigin.VERBOSE if "ipython-input-" in self.frame.file_name and self.name.startswith(
                "_" ) else ELocalOrigin.NORMAL


class ITbFormatter:
    """
    Something capable of formatting a traceback.
    See `format_traceback`.
    
    Should be considered single-threaded.
    
    !ABSTRACT
    """

    def format_traceback( self, tb_co: TracebackCollection, message: str, style: EStyle, ref: Optional[str] ) -> str:
        """
        Formats the traceback.
        """
        raise NotImplementedError( "abstract" )


class _TbFormatter( ITbFormatter ):
    """
    !ABSTRACT !OVERRIDE
    
    :ivar style:    State of current formatting. Style (see `EStyle`)
    :ivar reason:   State of current formatting. Reason for displaying traceback message
    :ivar output:   State of current formatting. Output buffer.   
    :ivar tb_co:    State of current formatting. Traceback object.
    """

    def __init__( self ):
        self.style: Optional[EStyle] = None
        self.reason: Optional[str] = None
        self.ref: Optional[str] = None
        self.output: Optional[List[str]] = None
        self.tb_co: Optional[TracebackCollection] = None

    def format_traceback( self, tb_co: TracebackCollection, reason: str, style: EStyle, ref: Optional[str] ) -> str:
        """
        !FINAL !OVERRIDE
        """
        if reason and reason[-1].isalnum():
            reason += "."

        # Set state
        self.style = style
        self.reason = reason
        self.ref = ref
        self.tb_co = tb_co
        self.output = []

        # Perform
        self.write_traceback()

        # Convert output to string
        return "".join( self.output )

    def write_traceback( self ):
        """
        Write the traceback.
        
        The derived class should:
        
         * add required prefixes/postfixes.
         * call the base class to write the reason and individual exception traces.
        """
        for tb_ex in self.tb_co.exceptions:
            self.write_exception( tb_ex )

    def write_exception( self, tb_ex: _TbEx ):
        """
        Writes an individual traceback from the collection.
        
        The derived class should: 
        
        * add the reason text (self.message, probably only for the first exception in the chain)
        * add the exception text
        * add required prefixes/postfixes
        * call the base class to write the individual frames. 
        """
        for tb_fr in tb_ex.frames:
            self.write_frame( tb_fr )

    def write_frame( self, tb_fr: _TbFrame ):
        """
        Writes an individual frame.
        
        The derived class should:
        
        * add the frame location
        * add the frame code context
        * call the base class to write the individual locals.
        """
        los = [x for x in tb_fr.locals if x.origin != ELocalOrigin.VERBOSE]

        for lo in los:
            self.write_variable( lo )

    def write_variable( self, lo: _TbLocal ):
        """
        Writes a frame-local variable.
        
        The derived class should:
        
        * add the local text (mandatory).
        """
        raise NotImplementedError( "abstract" )

    def print( self, x = "", end = "\n" ):
        """
        A convenience function that emulates `print`.
        Sends the output to `self.output`.
        """
        self.output.append( x )
        self.output.append( end )


class _TextErrorFormatter( _TbFormatter ):
    """
    Formats exception traces as plain text.
    """
    tb_reason_conditions = { EStyle.ERROR, EStyle.INFORMATION }
    tb_traceback_conditions = { EStyle.ERROR, EStyle.INFORMATION }
    tb_summary_conditions = { EStyle.ERROR, EStyle.WARNING, EStyle.INFORMATION }

    def write_traceback( self ):
        self.print( f"***** START {self.style.name} *****" )
        self.print( "REASON {self.reason}" )
        super().write_traceback()
        self.print( f"***** END {self.style.name} *****" )

    def write_exception( self, tb_ex: _TbEx ):
        if tb_ex.is_cause:
            self.print( "...caused by..." )

        self.print()
        self.print( "TYPE " + tb_ex.type )
        self.print( "MESSAGE " + tb_ex.message )

        super().write_exception( tb_ex )

    def write_frame( self, tb_fr: _TbFrame ):
        # Location
        self.print( "{origin} E{exception} F{frame} File \"{file}\", line {line} in {function}" \
                    .format( origin = tb_fr.origin.name,
                             exception = tb_fr.exception.index,
                             frame = tb_fr.index,
                             file = tb_fr.file_name,
                             line = str( tb_fr.line_no ),
                             function = tb_fr.function ) )

        # Context
        self.print( "CODE " + tb_fr.code_context )
        super().write_frame( tb_fr )

    def write_variable( self, lo: _TbLocal ):
        if len( lo.repr ) > 80:
            self.print( "LOCAL " + lo.name + " = \\" )
            self.print( lo.repr )
        else:
            self.print( "LOCAL " + lo.name + " = " + lo.repr )


class _HtmlTbFormatter( _TbFormatter ):
    """
    Formats exception traces as HTML.
    """
    tb_reason_conditions = { EStyle.ERROR, EStyle.INFORMATION, EStyle.WARNING }
    tb_traceback_conditions = { EStyle.ERROR, EStyle.INFORMATION, EStyle.WARNING }
    tb_summary_conditions = set()
    CSS = """
        .mhef_exception details summary::-webkit-details-marker 
        {
            display: none;
        }
        
        .mhef_exception details summary
        {
            outline:none;
        }
        
        .mhef_exception details summary:hover
        {
            box-shadow: 2px 2px 2px black;
            filter: brightness(110%);
        }
        
        
        
        .mhef_local_repr
        {
            text-align: left !important;
        }
        .mhef_local_name
        {
            color: #000080;
        }
        .mhef_local_type
        {
            font-style: italic;
        }
        .mhef_function
        {
            font-size: 10px;
            font-family: monospace;
            color: #0000FF;
        }
        
        .mhef_ex_type
        {
            font-family: monospace;
            padding: 8px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        
        .mhef_error .mhef_ex_type
        {
            background: #FF8080;
        }
        
        .mhef_warning .mhef_ex_type
        {
            background: #C0C080;
        }
        
        .mhef_ex_message
        {
            font-family: monospace;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            padding: 8px;
        }
        
        .mhef_error .mhef_ex_message
        {
            border: 1px solid #FF8080;
            background: #FFE0E0;
        }
        
        .mhef_warning .mhef_ex_message
        {
            border: 1px solid #C0C080;
            background: #FFFFE0;
        }        
        
        .mhef_code_context
        {
            font-size: 10px;
            font-family: monospace;
            display: block;
            color: #000080;
            border: 1px solid #000080;
            background: #FFFFFF;
            padding: 4px;
        }
            
        .mhef_frame_location
        {
            border: 1px solid black;
        }
        
        .mhef_file_name
        {
            text-decoration: underline;
        }
        
        .mhef_frame_origin_user
        {
            background: #E0E0FF;
        }
        .mhef_frame_origin_core
        {
            background: #C0C0C0;
            opacity: 0.25;
        }
        
        .mhef_frame_origin_set
        {
            background: #C0C0C0;
            color: #000000;
            margin: 2px;
            border: 1px outset #C0C0C0;
        }
        
        details[open] > .mhef_frame_origin_set
        {
            background: #808080;
            border: 1px inset #C0C0C0;
        }
        
        details > summary > div > .mhef_ex_cause
        {
        opacity: 0.5;
        }
        
        details > summary > div > .mhef_ex_cause:hover
        {
        opacity: 1;
        }
        
        .mhef_exception_details
        {
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            background: rgba(255, 128, 128, 0.1);
            border: 1px solid #FF8080;
            border-top: none;
            padding: 4px;
            padding-top: 0;
            margin: 4px;
            margin-top: 0;
        }
        
        div.mhef_ex_type > span.mhef_ex_cause
        {
        display: none;
        }
        
        div.mhef_ex_type:hover > span.mhef_ex_cause
        {
        display: inline;
        }
        """

    def __init__( self ):
        super().__init__()
        self.frame_origin = None

    def escape( self, x: object ):
        import html
        x = html.escape( str( x ) )
        x = x.replace( "\n", "<br/>" )
        self.print( x )

    def div( self, c: str, x: object ):
        self.print( f"<div class='{c}'>" )
        self.escape( x )
        self.print( "</div>" )

    def span( self, c: str, x: object ):
        self.print( f"<span class='{c}'>" )
        self.escape( x )
        self.print( "</span>" )

    def write_traceback( self ):
        self.print( f"<style>{self.CSS}</style>" )
        self.print( f"<div class='mhef_exception mhef_{self.style.name.lower()}'>" )
        super().write_traceback()

        for _ in self.tb_co.exceptions:
            self.print( "</div>" )
            self.print( "</details>" )

        self.print( "</div>" )

    def write_exception( self, tb_ex: _TbEx ):
        self.print( "<details>" )
        self.print( "<summary>" )

        #
        # Exception type
        #
        self.print( "<div class='mhef_ex_type'>" )
        self.escape( tb_ex.type )

        msg = f"({tb_ex.index + 1} of {tb_ex.collection.exceptions.__len__()})"

        if tb_ex.is_cause:
            self.print(
                    f"<span title='This exception is the cause of the preceding exception.' class='mhef_ex_cause'>{msg}</span>" )
        else:
            import html
            reason = html.escape( self.reason )
            self.print( f"<span title='{reason}' class='mhef_ex_cause'>{msg}</span>" )

        self.print( "</div>" )

        self.print( "<div class = 'mhef_ex_message'>" )
        self.escape( tb_ex.message )
        self.print( "</div>" )

        self.print( "</summary>" )

        self.frame_origin = None

        self.print( "<div class='mhef_exception_details'>" )

        super().write_exception( tb_ex )
        self.finish_frame_origin()

    def finish_frame_origin( self ):
        if self.frame_origin is not None:
            self.print( "</details>" )

    def write_frame( self, tb_fr: _TbFrame ):
        if tb_fr.origin != self.frame_origin:
            self.finish_frame_origin()
            self.frame_origin = tb_fr.origin

            open_ = "open" if tb_fr.origin not in (_EFrameOrigin.SYSTEM, _EFrameOrigin.SITE) else ""
            self.print(
                    f"<details {open_}><summary><span class='mhef_frame_origin_set'>{tb_fr.origin.name} frames</span></summary>" )

        self.print( "<details><summary>" )

        # Location
        self.print( f"<div class='mhef_frame_location mhef_frame_origin_{tb_fr.origin.name.lower()}'>" )
        self.span( "mhef_origin", tb_fr.origin.name )
        self.span( "mhef_ex_index", tb_fr.exception.index )
        self.span( "mhef_fr_index", tb_fr.index )
        self.span( "mhef_file_name", tb_fr.file_name )
        self.span( "mhef_line_no", tb_fr.line_no )
        self.span( "mhef_function", tb_fr.function )
        self.print( "</div>" )

        # Context
        self.print( "<div class='mhef_code_context'>" )
        self.escape( tb_fr.code_context )
        self.print( "</div>" )

        self.print( "</summary>" )

        # Locals
        self.print( "<table class='mhef_frame_locals'>" )
        super().write_frame( tb_fr )
        self.print( "</table>" )
        self.print( "</details>" )

    def write_variable( self, lo: _TbLocal ):
        self.print( "<tr>" )
        self.print( "<td class='mhef_local_index'>" )
        self.print( str( lo.index ) )
        self.print( "</td><td class='mhef_local_name'>" )
        self.escape( lo.name )
        self.print( "</td><td class='mhef_local_type'>" )
        self.escape( lo.value.__class__.__name__ )
        self.print( "</td><td class='mhef_local_repr'>" )
        self.escape( lo.repr )
        self.print( "</td></tr>" )


class _AnsiErrorFormatter( _TbFormatter ):
    """
    Formats exception traces as ANSI text.
    """
    tb_reason_conditions = { EStyle.ERROR, EStyle.INFORMATION }
    tb_traceback_conditions = { EStyle.ERROR, EStyle.INFORMATION }
    tb_summary_conditions = { EStyle.ERROR, EStyle.INFORMATION, EStyle.WARNING }

    title_bar = ansi.back( 255, 0, 255 ) + " " + ansi.RESET + " "
    frame_bar = ansi.back( 255, 0, 0 ) + " " + ansi.RESET + " "
    context_bar = ansi.back( 0, 255, 255 ) + " " + ansi.RESET + " "
    locals_bar = ansi.back( 0, 0, 64 ) + "    " + ansi.RESET + " "

    error_key = ansi.FORE_WHITE + ansi.BACK_RED
    warning_key = ansi.FORE_BLACK + ansi.BACK_YELLOW
    information_key = ansi.FORE_WHITE + ansi.BACK_BLUE

    reset_colour = ansi.RESET

    extra_colour = ansi.fore( 128, 128, 128 )

    title_colour = ansi.FORE_BRIGHT_WHITE
    title_type_colour = ansi.FORE_BRIGHT_WHITE + ansi.UNDERLINE

    local_name_colour = ansi.FORE_BRIGHT_CYAN
    local_type_colour = ansi.FORE_BRIGHT_BLACK
    local_value_colour = ansi.FORE_BRIGHT_BLUE

    code_colour = ansi.FORE_RED
    code_function_colour = ansi.FORE_BRIGHT_RED

    inside_file_colour = ansi.FORE_YELLOW
    inside_name_colour = ansi.FORE_BRIGHT_YELLOW

    outside_file_colour = ansi.FORE_BRIGHT_BLACK
    outside_file_name_colour = ansi.FORE_WHITE

    def write_traceback( self ):
        ref = f" {self.ref}" if self.ref else ""

        self.__styled_message( f"START OF {self.style.name} MESSAGE{ref}" )

        if self.style != EStyle.WARNING:
            self.write_msg( message = self.reason or "",
                            colour = self.extra_colour,
                            level = self.title_bar )

            super().write_traceback()

        for tb_ex in self.tb_co.exceptions:
            self.write_exception( tb_ex, _title_only = True )

        if self.style == EStyle.ERROR:
            self.output.append( "\a" )  # bell

        self.__styled_message( f"END OF {self.style.name} MESSAGE{ref}" )

    def write_msg( self, *, message: str, colour: str, level ):
        # from mhelper.ansi_helper import wrap

        lines = message.split( "\n" )

        for line in lines:
            self.output.append( f"{level}{colour}{line}{self.reset_colour}\n" )

        # for l in wrap( message, self.width, justify = justify ):
        #     self.output.append( self.left_margin + colour + " " + colour2 + l + colour + " " + self.right_margin )

    def write_exception( self, tb_ex: _TbEx, _title_only = False ):
        # Format: Caused by...
        if tb_ex.is_cause:
            self.write_msg( message = "caused by",
                            colour = self.extra_colour,
                            level = self.title_bar )
        # ...end

        # Format: Title...
        self.write_msg( message = f"",
                        colour = self.title_colour,
                        level = self.title_bar )
        self.write_msg( message = f"{tb_ex.type}",
                        colour = self.title_type_colour,
                        level = self.title_bar )
        self.write_msg( message = f"{tb_ex.message}\n",
                        colour = self.title_colour,
                        level = self.title_bar )

        if not _title_only:
            super().write_exception( tb_ex )

    def write_frame( self, tb_fr: _TbFrame ):
        #
        # LOCATION
        #

        # Format: Location...
        if tb_fr.origin == _EFrameOrigin.SYSTEM:
            fc = self.outside_file_colour
            fbc = self.outside_file_name_colour
        elif tb_fr.origin == _EFrameOrigin.SITE:
            fc = self.outside_file_colour
            fbc = self.outside_file_name_colour
        else:
            fc = self.inside_file_colour
            fbc = self.inside_name_colour

        # File "/home/mjr/work/mhelper/mhelper/string_helper.py", line 792, in wrap
        self.write_msg( message = "E{exception} F{frame} File \"{file}\", line {line} in {function}" \
                        .format( exception = tb_fr.exception.index,
                                 frame = tb_fr.index,
                                 file = fbc + tb_fr.file_name + fc,
                                 line = fbc + str( tb_fr.line_no ) + fc,
                                 function = fbc + tb_fr.function ),
                        colour = fc,
                        level = self.frame_bar )

        #
        # CONTEXT
        #
        self.write_msg( message = (tb_fr.code_context.replace( tb_fr.next_function,
                                                               self.code_function_colour + tb_fr.next_function + self.code_colour )
                                   if tb_fr.next_function
                                   else tb_fr.code_context),
                        colour = self.code_colour,
                        level = self.context_bar )

        #
        # LOCALS
        #
        super().write_frame( tb_fr )

    def write_variable( self, lo: _TbLocal ):
        t = type( lo.value )
        tn = t.__name__

        if lo.repr.startswith( tn ) or t in (str, bool, float, int, type( None )):
            name = lo.name
        else:
            name = f"{lo.name}{self.local_type_colour}:{tn} "

        if len( lo.repr ) > 80 or "\n" in lo.repr:
            self.write_msg( message = name + "=-",
                            colour = self.local_name_colour,
                            level = self.locals_bar )
            self.write_msg( message = string_helper.hard_wrap( lo.repr, 80 ),
                            colour = self.local_value_colour,
                            level = self.locals_bar )
        else:
            self.write_msg( message = name + "= " + self.local_value_colour + lo.repr,
                            colour = self.local_name_colour,
                            level = self.locals_bar )

    def __styled_message( self, prefix ):
        if self.style == EStyle.ERROR:
            self.write_msg( message = f"////////// {prefix} //////////",
                            colour = self.error_key,
                            level = "" )
        elif self.style == EStyle.WARNING:
            self.write_msg( message = f"////////// {prefix} //////////",
                            colour = self.warning_key,
                            level = "" )
        elif self.style == EStyle.INFORMATION:
            self.write_msg( message = f"////////// {prefix} //////////",
                            colour = self.information_key,
                            level = "" )
        else:
            raise ValueError( "Invalid style." )


_TProduct = TypeVar( "_TProduct" )
_Factory = Union[_TProduct, Type[_TProduct], Callable[[], _TProduct]]

_FORMAT_MAP = { EFormat.ANSI: _AnsiErrorFormatter,
                EFormat.TEXT: _TextErrorFormatter,
                EFormat.HTML: _HtmlTbFormatter }


def format_traceback( exception: Optional[BaseException],
                      message: str,
                      style: Union[EStyle, str, int] = EStyle.ERROR,
                      format: Union[EFormat, str, int, _Factory[ITbFormatter]] = EFormat.ANSI,
                      ref: Optional[str] = None
                      ) -> str:
    """
    Formats a traceback for an exception and its causes.
    
    :param exception:   Exception.
                        `None` uses the last traceback. 
    :param message:     Message, provided as the reason for displaying the
                        traceback.  
    :param style:       Style of traceback to produce.
                        A member of the `EStyle` enum, its name, or its value.
    :param format:      Format to produce the traceback in.
                        A member of the `EFormat` enum, its name, or its value,
                        or an `ITbFormatter` instance or factory.
    :param ref:         Reference to be inserted into message.
                        This is not the same as `print_traceback`'s ref
                        parameter, which *generates* the ref.
    :return:            Traceback as a string.
    """
    from mhelper.enum_helper import map_enum

    # Map style
    style = map_enum( EStyle, style )

    # Map format
    if isinstance( format, EFormat ) or isinstance( format, str ) or isinstance( format, int ):
        oformat = format
        format = map_enum( EFormat, format )

        # The following fixes a rather esoteric problem where we reload the
        # enum class, usually via %load_ext autoreload in Jupyter. Since Enum
        # relies on object identity v = Enum.Value may not be equal to
        # Enum.Value if the class was reloaded after v's assignment.
        format = EFormat[format.name]

        try:
            format = _FORMAT_MAP[format]
        except KeyError as ex:
            raise ValueError( f"The format cannot be found in the format map and"
                              " doesn't appear to be a factory.\n"
                              "Please check the argument.\n"
                              f"Format = {format!r}\n"
                              f"Format type = {format.__class__.__name__}\n"
                              f"Mapped from = {oformat!r}\n"
                              f"Format map = {_FORMAT_MAP!r}" ) from ex

    if not isinstance( format, ITbFormatter ):
        format = format()

    tb_co = get_traceback_ex( exception )
    return format.format_traceback( tb_co, message, style, ref )


format_traceback_ex = format_traceback  # Deprecated alias


def get_traceback_ex( ex: BaseException ) -> TracebackCollection:
    """
    Gets a `TracebackCollection` from an exception.
    
    :param ex:  Exception, or `None` to use the last exception.  
    :return:    Traceback collection for the exception and its causes.
    """
    tb_co = TracebackCollection()

    if ex is None:
        ex = sys.exc_info()[1]

    causes: List[Tuple[int, BaseException]] = []

    while ex is not None:
        causes.append( (len( causes ), ex) )
        ex = ex.__cause__

    for i, ex in causes:
        tb_ex = _TbEx( tb_co, i, ex )
        tb_co.exceptions.append( tb_ex )

        tb = ex.__traceback__

        before: Iterable[Tuple[int, FrameInfo]]
        after: Iterable[Tuple[int, FrameInfo]]

        if tb is None:
            # Exceptions from warnings won't have a traceback, so just use the
            # current stack trace - it will have the warning in somewhere!
            before = reversed( [(-1 - i, x) for i, x in enumerate( inspect.stack()[1:] )] )
            after = ()
        else:
            before = reversed( [(-1 - i, x) for i, x in enumerate( inspect.getouterframes( tb.tb_frame )[1:] )] )
            after = enumerate( inspect.getinnerframes( tb ) )

        prev_frame = None

        for index, frame in itertools.chain( before, after ):
            tb_fr = _TbFrame( tb_ex, index, frame )
            tb_ex.frames.append( tb_fr )

            if prev_frame is not None:
                prev_frame.next_function = tb_fr.function

            for index_2, (key, value) in enumerate( frame.frame.f_locals.items() ):
                try:
                    from mhelper.debug_helper import str_repr
                except Exception:
                    str_repr = lambda x: f"(APPROX-REPR?)({x!r})"

                rep = str_repr( value )

                if len( rep ) > 1024:
                    rep = rep[:1024] + "..."

                tb_lo = _TbLocal( tb_fr, index_2, key, value, rep )
                tb_fr.locals.append( tb_lo )

    return tb_co



