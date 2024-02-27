"""
This package defines constants for ANSI-terminal escape sequences.
There are also functions for generating escape sequences, such as 24-bit colour
codes.

Please note that this package only defines codes, it does not guarantee support
for their correct interpretation in the terminal (there is the `colorama`
package which does that).

To test on your terminal::

    python -m mhelper._unittests.test_ansi
    
.. note::

    The "bright" and "light" versions are identical. "bright" is the ANSI name,
    and is a more accurate description on traditional terminals and Windows, 
    while "light" is what the `colorama` package calls them, and is a more accurate
    description for Linux terminal emulators.
    
.. note:

    Comments shown describe support for three terminals: The [W]indows console
    (Cmd, LSW or PowerShell, with ANSI enabled), [I]term2 and [K]onsole. The
    PowerShell ISE does not support any ANSI.
"""
# !EXPORT_TO_README

# 
from mhelper import colours


ESC = "\033"

RESET = "\033[0m"

# Styles
BOLD = "\033[1m"  #             W: Changes colour       K: Does not work with most fonts.
DIM = "\033[2m"  #              W: No                   K: Poor implementation 
ITALIC = "\033[3m"  #           W: No                   K: ?
UNDERLINE = "\033[4m"  #        W: Yes                  K: ?
BLINK = "\033[5m"  #            W: No                   K: ?
INVERSE = "\033[7m"  #          W: Yes                  K: ?
CONCEAL = "\033[8m"  #          W: No                   K: ?
STRIKETHROUGH = "\033[9m"  #    W: No                   K: ?

NORMAL = "\033[22m"
BOLD_OFF = "\033[22m"
DIM_OFF = "\033[22m"
ITALIC_OFF = "\033[23m"
UNDERLINE_OFF = "\033[24m"
BLINK_OFF = "\033[25m"
INVERSE_OFF = "\033[27m"
CONCEAL_OFF = "\033[28m"
STRIKETHROUGH_OFF = "\033[29m"

# Fonts                         W: No                   K: No           I: No
FONT_0 = "\033[10m"
FONT_1 = "\033[11m"
FONT_2 = "\033[12m"
FONT_3 = "\033[13m"
FONT_4 = "\033[14m"
FONT_5 = "\033[15m"
FONT_6 = "\033[16m"
FONT_7 = "\033[17m"
FONT_8 = "\033[18m"
FONT_9 = "\033[19m"
FRAKTUR = "\033[20m"

# Foreground
FORE_BLACK = "\033[30m"
FORE_RED = "\033[31m"
FORE_GREEN = "\033[32m"
FORE_YELLOW = "\033[33m"
FORE_BLUE = "\033[34m"
FORE_MAGENTA = "\033[35m"
FORE_CYAN = "\033[36m"
FORE_WHITE = "\033[37m"
FORE_RESET = "\033[39m"
FORE_BRIGHT_BLACK = "\033[90m"
FORE_BRIGHT_RED = "\033[91m"
FORE_BRIGHT_GREEN = "\033[92m"
FORE_BRIGHT_YELLOW = "\033[93m"
FORE_BRIGHT_BLUE = "\033[94m"
FORE_BRIGHT_MAGENTA = "\033[95m"
FORE_BRIGHT_CYAN = "\033[96m"
FORE_BRIGHT_WHITE = "\033[97m"

# Background
BACK_BLACK = "\033[40m"
BACK_RED = "\033[41m"
BACK_GREEN = "\033[42m"
BACK_YELLOW = "\033[43m"
BACK_BLUE = "\033[44m"
BACK_MAGENTA = "\033[45m"
BACK_CYAN = "\033[46m"
BACK_WHITE = "\033[47m"
BACK_RESET = "\033[49m"
BACK_LIGHT_BLACK = "\033[100m"
BACK_LIGHT_RED = "\033[101m"
BACK_LIGHT_GREEN = "\033[102m"
BACK_LIGHT_YELLOW = "\033[103m"
BACK_LIGHT_BLUE = "\033[104m"
BACK_LIGHT_MAGENTA = "\033[105m"
BACK_LIGHT_CYAN = "\033[106m"
BACK_LIGHT_WHITE = "\033[107m"
BACK = [BACK_BLACK,
        BACK_RED,
        BACK_GREEN,
        BACK_YELLOW,
        BACK_BLUE,
        BACK_MAGENTA,
        BACK_CYAN,
        BACK_WHITE]

# "Bright" for synonomy with colourama, though these colours are typically lighter rather than brighter
BACK_BRIGHT_BLACK = "\033[100m"
BACK_BRIGHT_RED = "\033[101m"
BACK_BRIGHT_GREEN = "\033[102m"
BACK_BRIGHT_YELLOW = "\033[103m"
BACK_BRIGHT_BLUE = "\033[104m"
BACK_BRIGHT_MAGENTA = "\033[105m"
BACK_BRIGHT_CYAN = "\033[106m"
BACK_BRIGHT_WHITE = "\033[107m"

# Miscellaneous codes
CLEAR_SCREEN = "\033[2J"
ALTERNATE_SCREEN = "\033[?1049h\033[H"
ALTERNATE_SCREEN_OFF = "\033[?1049l"


# 24-bit colours
def fore( *args ) -> str:
    """
    Generates ANSI sequence for setting the foreground colour.
    
    `args` may be any value accepted by `Colour.use`.
    
    The following values are additionally supported:
    
    * ANSI escape code   - ANSI escape code (returned verbatim)
    * None               - Returns an empty string
    * Colour.Transparent - Returns the reset colour code
    """
    if len( args ) == 1 and isinstance( args[0], str ) and args[0].startswith( "\033" ):
        return args[0]
    
    from mhelper.colours import Colour
    c = Colour.use( *args )
    
    if c is None:
        return ""
    
    if not c.a:
        return FORE_RESET
    
    return "\033[38;2;" + str( int( c.r ) ) + ";" + str( int( c.g ) ) + ";" + str( int( c.b ) ) + "m"


def back( *args ) -> str:
    """
    Generates ANSI sequence for setting the background colour.
    Pamameters are the same as `fore`.
    """
    if len( args ) == 1 and isinstance( args[0], str ) and args[0].startswith( "\033" ):
        return args[0]
    
    from mhelper.colours import Colour
    c = Colour.use( *args )
    
    if c is None:
        return ""
    
    if not c.a:
        return BACK_RESET
    
    return "\033[48;2;" + str( int( c.r ) ) + ";" + str( int( c.g ) ) + ";" + str( int( c.b ) ) + "m"


def move( r: int, c: int ) -> str:
    """
    Generates ANSI sequence for moving the cursor.
    The top-left character is (1, 1).
    
    :param r:   Row (Y) 
    :param c:   Column (X) 
    :return:    Code 
    """
    return f"\033[{r};{c}H"


# Text
X = RESET

FR = FORE_RED
FG = FORE_GREEN
FB = FORE_BLUE
FC = FORE_CYAN
FY = FORE_YELLOW
FM = FORE_MAGENTA
FW = FORE_WHITE
FK = FORE_BLACK

FBR = FORE_BRIGHT_RED
FBG = FORE_BRIGHT_GREEN
FBB = FORE_BRIGHT_BLUE
FBC = FORE_BRIGHT_CYAN
FBY = FORE_BRIGHT_YELLOW
FBM = FORE_BRIGHT_MAGENTA
FBW = FORE_BRIGHT_WHITE
FBK = FORE_BRIGHT_BLACK

# Background
BR = BACK_RED
BG = BACK_GREEN
BB = BACK_BLUE
BC = BACK_CYAN
BY = BACK_YELLOW
BM = BACK_MAGENTA
BW = BACK_WHITE
BK = BACK_BLACK

BBR = BACK_LIGHT_RED
BBG = BACK_LIGHT_GREEN
BBB = BACK_LIGHT_BLUE
BBC = BACK_LIGHT_CYAN
BBY = BACK_LIGHT_YELLOW
BBM = BACK_LIGHT_MAGENTA
BBW = BACK_LIGHT_WHITE
BBK = BACK_LIGHT_BLACK

# Styles
SB = BOLD
SD = DIM
SI = ITALIC
SU = UNDERLINE
SE = INVERSE


class Fore:
    __slots__ = ()
    BLACK = FORE_BLACK
    RED = FORE_RED
    GREEN = FORE_GREEN
    YELLOW = FORE_YELLOW
    BLUE = FORE_BLUE
    MAGENTA = FORE_MAGENTA
    CYAN = FORE_CYAN
    WHITE = FORE_WHITE
    LIGHT_BLACK = BRIGHT_BLACK = FORE_BRIGHT_BLACK
    LIGHT_RED = BRIGHT_RED = FORE_BRIGHT_RED
    LIGHT_GREEN = BRIGHT_GREEN = FORE_BRIGHT_GREEN
    LIGHT_YELLOW = BRIGHT_YELLOW = FORE_BRIGHT_YELLOW
    LIGHT_BLUE = BRIGHT_BLUE = FORE_BRIGHT_BLUE
    LIGHT_MAGENTA = BRIGHT_MAGENTA = FORE_BRIGHT_MAGENTA
    LIGHT_CYAN = BRIGHT_CYAN = FORE_BRIGHT_CYAN
    LIGHT_WHITE = BRIGHT_WHITE = FORE_BRIGHT_WHITE
    RESET = FORE_RESET


class Back:
    __slots__ = ()
    BLACK = BACK_BLACK
    RED = BACK_RED
    GREEN = BACK_GREEN
    YELLOW = BACK_YELLOW
    BLUE = BACK_BLUE
    MAGENTA = BACK_MAGENTA
    CYAN = BACK_CYAN
    WHITE = BACK_WHITE
    RESET = BACK_RESET
    LIGHT_BLACK = BACK_LIGHT_BLACK
    LIGHT_RED = BACK_LIGHT_RED
    LIGHT_GREEN = BACK_LIGHT_GREEN
    LIGHT_YELLOW = BACK_LIGHT_YELLOW
    LIGHT_BLUE = BACK_LIGHT_BLUE
    LIGHT_MAGENTA = BACK_LIGHT_MAGENTA
    LIGHT_CYAN = BACK_LIGHT_CYAN
    LIGHT_WHITE = BACK_LIGHT_WHITE


_H = 192
_h = 0
_f = 0
_F = 255


class Back24:
    __slots__ = ()
    BLACK = back( _h, _h, _h )
    RED = back( _H, _h, _h )
    GREEN = back( _h, _H, _h )
    YELLOW = back( _H, _H, _h )
    BLUE = back( _h, _h, _H )
    MAGENTA = back( _H, _h, _H )
    CYAN = back( _h, _H, _H )
    WHITE = back( _H, _H, _H )
    LIGHT_BLACK = BRIGHT_BLACK = back( _f, _f, _f )
    LIGHT_RED = BRIGHT_RED = back( _F, _f, _f )
    LIGHT_GREEN = BRIGHT_GREEN = back( _f, _F, _f )
    LIGHT_YELLOW = BRIGHT_YELLOW = back( _F, _F, _f )
    LIGHT_BLUE = BRIGHT_BLUE = back( _f, _f, _F )
    LIGHT_MAGENTA = BRIGHT_MAGENTA = back( _F, _f, _F )
    LIGHT_CYAN = BRIGHT_CYAN = back( _f, _F, _F )
    LIGHT_WHITE = BRIGHT_WHITE = back( _F, _F, _F )
    RESET = BACK_RESET


class Fore24:
    __slots__ = ()
    BLACK = fore( _h, _h, _h )
    RED = fore( _H, _h, _h )
    GREEN = fore( _h, _H, _h )
    YELLOW = fore( _H, _H, _h )
    BLUE = fore( _h, _h, _H )
    MAGENTA = fore( _H, _h, _H )
    CYAN = fore( _h, _H, _H )
    WHITE = fore( _H, _H, _H )
    BRIGHT_BLACK = LIGHT_BLACK = fore( _f, _f, _f )
    BRIGHT_RED = LIGHT_RED = fore( _F, _f, _f )
    BRIGHT_GREEN = LIGHT_GREEN = fore( _f, _F, _f )
    BRIGHT_YELLOW = LIGHT_YELLOW = fore( _F, _F, _f )
    BRIGHT_BLUE = LIGHT_BLUE = fore( _f, _f, _F )
    BRIGHT_MAGENTA = LIGHT_MAGENTA = fore( _F, _f, _F )
    BRIGHT_CYAN = LIGHT_CYAN = fore( _f, _F, _F )
    BRIGHT_WHITE = LIGHT_WHITE = fore( _F, _F, _F )
    RESET = FORE_RESET


class Style:
    __slots__ = ()
    RESET_ALL = RESET
    BOLD = BOLD
    DIM = DIM
    ITALIC = ITALIC
    UNDERLINE = UNDERLINE
    BLINK = BLINK
    INVERSE = INVERSE
    CONCEAL = CONCEAL
    STRIKETHROUGH = STRIKETHROUGH
    NORMAL = NORMAL
    BOLD_OFF = BOLD_OFF
    DIM_OFF = DIM_OFF
    ITALIC_OFF = ITALIC_OFF
    UNDERLINE_OFF = UNDERLINE_OFF
    BLINK_OFF = BLINK_OFF
    INVERSE_OFF = INVERSE_OFF
    CONCEAL_OFF = CONCEAL_OFF
    STRIKETHROUGH_OFF = STRIKETHROUGH_OFF


def get_dos_colour_map():
    return {
        colours.Colours.BLACK       : (FORE_BLACK, BACK_BLACK),
        colours.Colours.DARK_RED    : (FORE_RED, BACK_RED),
        colours.Colours.DARK_GREEN  : (FORE_GREEN, BACK_GREEN),
        colours.Colours.DARK_YELLOW : (FORE_YELLOW, BACK_YELLOW),
        colours.Colours.DARK_BLUE   : (FORE_BLUE, BACK_BLUE),
        colours.Colours.DARK_MAGENTA: (FORE_MAGENTA, BACK_MAGENTA),
        colours.Colours.DARK_CYAN   : (FORE_CYAN, BACK_CYAN),
        colours.Colours.LIGHT_GRAY  : (FORE_WHITE, BACK_WHITE),
        colours.Colours.DARK_GRAY   : (FORE_BRIGHT_BLACK, BACK_BRIGHT_BLACK),
        colours.Colours.RED         : (FORE_BRIGHT_RED, BACK_BRIGHT_RED),
        colours.Colours.GREEN       : (FORE_BRIGHT_GREEN, BACK_BRIGHT_GREEN),
        colours.Colours.YELLOW      : (FORE_BRIGHT_YELLOW, BACK_BRIGHT_YELLOW),
        colours.Colours.BLUE        : (FORE_BRIGHT_BLUE, BACK_BRIGHT_BLUE),
        colours.Colours.MAGENTA     : (FORE_BRIGHT_MAGENTA, BACK_BRIGHT_MAGENTA),
        colours.Colours.CYAN        : (FORE_BRIGHT_CYAN, BACK_BRIGHT_CYAN),
        colours.Colours.WHITE       : (FORE_BRIGHT_WHITE, BACK_BRIGHT_WHITE),
        }


# Esc[20h 	Set new line mode 	LMN
# Esc[?1h 	Set cursor key to application 	DECCKM
# none 	Set ANSI (versus VT52) 	DECANM
# Esc[?3h 	Set number of columns to 132 	DECCOLM
# Esc[?4h 	Set smooth scrolling 	DECSCLM
# Esc[?5h 	Set reverse video on screen 	DECSCNM
# Esc[?6h 	Set origin to relative 	DECOM
# Esc[?7h 	Set auto-wrap mode 	DECAWM
# Esc[?8h 	Set auto-repeat mode 	DECARM
# Esc[?9h 	Set interlacing mode 	DECINLM
#  
# Esc[20l 	Set line feed mode 	LMN
# Esc[?1l 	Set cursor key to cursor 	DECCKM
# Esc[?2l 	Set VT52 (versus ANSI) 	DECANM
# Esc[?3l 	Set number of columns to 80 	DECCOLM
# Esc[?4l 	Set jump scrolling 	DECSCLM
# Esc[?5l 	Set normal video on screen 	DECSCNM
# Esc[?6l 	Set origin to absolute 	DECOM
# Esc[?7l 	Reset auto-wrap mode 	DECAWM
# Esc[?8l 	Reset auto-repeat mode 	DECARM
# Esc[?9l 	Reset interlacing mode 	DECINLM
#  
# Esc= 	Set alternate keypad mode 	DECKPAM
# Esc> 	Set numeric keypad mode 	DECKPNM
#  
# Esc(A 	Set United Kingdom G0 character set 	setukg0
# Esc)A 	Set United Kingdom G1 character set 	setukg1
# Esc(B 	Set United States G0 character set 	setusg0
# Esc)B 	Set United States G1 character set 	setusg1
# Esc(0 	Set G0 special chars. & line set 	setspecg0
# Esc)0 	Set G1 special chars. & line set 	setspecg1
# Esc(1 	Set G0 alternate character ROM 	setaltg0
# Esc)1 	Set G1 alternate character ROM 	setaltg1
# Esc(2 	Set G0 alt char ROM and spec. graphics 	setaltspecg0
# Esc)2 	Set G1 alt char ROM and spec. graphics 	setaltspecg1
#  
# EscN 	Set single shift 2 	SS2
# EscO 	Set single shift 3 	SS3
#  
# Esc[m 	Turn off character attributes 	SGR0
# Esc[0m 	Turn off character attributes 	SGR0
# Esc[1m 	Turn bold mode on 	SGR1
# Esc[2m 	Turn low intensity mode on 	SGR2
# Esc[4m 	Turn underline mode on 	SGR4
# Esc[5m 	Turn blinking mode on 	SGR5
# Esc[7m 	Turn reverse video on 	SGR7
# Esc[8m 	Turn invisible text mode on 	SGR8
#  
# Esc[Line;Liner 	Set top and bottom lines of a window 	DECSTBM
#

def cursor_up( n ):
    return f"{ESC}[{n}A"


def cursor_down( n ):
    return f"{ESC}[{n}B"


def cursor_right( n ):
    return f"{ESC}[{n}C"


def cursor_left( n ):
    return f"{ESC}[{n}D"


# Esc[H 	Move cursor to upper left corner 	cursorhome
# Esc[;H 	Move cursor to upper left corner 	cursorhome
# Esc[Line;ColumnH 	Move cursor to screen location v,h 	CUP
# Esc[f 	Move cursor to upper left corner 	hvhome
# Esc[;f 	Move cursor to upper left corner 	hvhome
# Esc[Line;Columnf 	Move cursor to screen location v,h 	CUP
# EscD 	Move/scroll window up one line 	IND
# EscM 	Move/scroll window down one line 	RI
# EscE 	Move to next line 	NEL
# Esc7 	Save cursor position and attributes 	DECSC
# Esc8 	Restore cursor position and attributes 	DECSC
#  
# EscH 	Set a tab at the current column 	HTS
# Esc[g 	Clear a tab at the current column 	TBC
# Esc[0g 	Clear a tab at the current column 	TBC
# Esc[3g 	Clear all tabs 	TBC
#  
# Esc#3 	Double-height letters, top half 	DECDHL
# Esc#4 	Double-height letters, bottom half 	DECDHL
# Esc#5 	Single width, single height letters 	DECSWL
# Esc#6 	Double width, single height letters 	DECDWL
#

CLEAR_LINE_RIGHT = f"{ESC}[0K"  # also Esc[K
CLEAR_LINE_LEFT = f"{ESC}[1K"
CLEAR_LINE = f"{ESC}[2K"

# Esc[J 	Clear screen from cursor down 	ED0
# Esc[0J 	Clear screen from cursor down 	ED0
# Esc[1J 	Clear screen from cursor up 	ED1
# Esc[2J 	Clear entire screen 	ED2
#  
# Esc5n 	Device status report 	DSR
# Esc0n 	Response: terminal is OK 	DSR
# Esc3n 	Response: terminal is not OK 	DSR
#  
# Esc6n 	Get cursor position 	DSR
# EscLine;ColumnR 	Response: cursor is at v,h 	CPR
#  
# Esc[c 	Identify what terminal type 	DA
# Esc[0c 	Identify what terminal type (another) 	DA
# Esc[?1;Value0c 	Response: terminal type code n 	DA
#  
# Escc 	Reset terminal to initial state 	RIS
#  
# Esc#8 	Screen alignment display 	DECALN
# Esc[2;1y 	Confidence power up test 	DECTST
# Esc[2;2y 	Confidence loopback test 	DECTST
# Esc[2;9y 	Repeat power up test 	DECTST
# Esc[2;10y 	Repeat loopback test 	DECTST
#  
# Esc[0q 	Turn off all four leds 	DECLL0
# Esc[1q 	Turn on LED #1 	DECLL1
# Esc[2q 	Turn on LED #2 	DECLL2
# Esc[3q 	Turn on LED #3 	DECLL3
# Esc[4q 	Turn on LED #4 	DECLL4
