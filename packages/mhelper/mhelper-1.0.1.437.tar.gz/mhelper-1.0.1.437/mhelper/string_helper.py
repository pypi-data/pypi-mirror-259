"""
Functions for parsing strings into objects and generating strings from objects.

Also contains `TStr` functions that replicate several of Python's `str` methods.
Unlike `str`, `TStr` permits an duck-typed object behaving *like* a `str`,
rather than enforcing a `str` specifically.

:data FormatDelegate: A public union that specifies types acceptable to `format_delegate`.
"""
# !EXPORT_TO_README

import datetime
import itertools
import math
import random
import re
import warnings
from collections import Counter, defaultdict
from enum import Enum, Flag
from itertools import zip_longest, count
from typing import Callable, Iterable, Iterator, List, Optional, overload, Union, cast, Sequence, Type, TypeVar, Set, \
    Any, Dict, Tuple

from mhelper import array_helper
from mhelper.special_types import NOT_PROVIDED

__author__ = "Martin Rusilowicz"

_T = TypeVar( "_T" )
_U = TypeVar( "_U" )
_TSimple = TypeVar( "_TSimple", int, str, float, bool, Flag, Enum )
_TEnum = TypeVar( "_TEnum", bound=Enum )
_TFlag = TypeVar( "_TFlag", bound=Flag )
_TStr = TypeVar( "_TStr", bound=str )
__strip_lines_rx = re.compile( r"^[ ]+", re.MULTILINE )
__word_delimiter_rx = re.compile( r"([" + re.escape( "\t\n\x0b\x0c\r " ) + r"]+)" )
__shrink_space_rx = re.compile( r"\s+" )

FormatDelegate = Union[str, Callable[[object], str]]


def regex_extract( regex, text, group=1, default="" ) -> str:
    """
    Obtains the text matching a regular expression.
    """
    m = re.search( regex, text )

    if m is None:
        return default

    return m.group( group )


def highlight_regex( text, regex, colour, normal, group=1 ) -> str:
    """
    Highlights text matching a regular expression.
    """
    l = len( colour ) + len( normal )

    for i, m in enumerate( re.finditer( regex, text, re.IGNORECASE ) ):
        if group > m.lastindex:
            continue

        s = m.start( group ) + l * i
        e = m.end( group ) + l * i

        text = text[:s] + colour + text[s:e] + normal + text[e:]

    return text


def highlight_quotes( text, start, end, colour, normal, count=0 ):
    """
    Highlights text surrounded by quotes.
    """
    start = re.escape( start )
    end = re.escape( end )
    find = start + "([^" + start + end + "]+)" + end
    replace = colour + "\\1" + normal
    return re.sub( find, replace, text, count=count )


def curtail( text: str, start: Optional[str] = None, end: Optional[str] = None, error=False ) -> str:
    """
    Removes text from the start or end of a string
    """
    if start:
        if text.startswith( start ):
            text = text[len( start ):]
        elif error:
            raise KeyError(
                "Trying to remove the substring «{0}» from the string «{1}» but the string does not start with the substring.".format(
                    start, text ) )

    if end:
        if text.endswith( end ):
            text = text[:len( text ) - len( end )]
        elif error:
            raise KeyError(
                "Trying to remove the substring «{0}» from the string «{1}» but the string does not end with the substring.".format(
                    end, text ) )

    return text


def percent_to_string( n: float = None, d: float = None, q=None, t=0, dp: int = 0 ):
    """
    Formats a value percentage from either the quotient (Q), the numerator (N) and/or the denominator (D).
    
    OVERLOADS
    ---------

    ```
    percent( q,         t = 1 )                  # N and D unknown, defaults to `t = 1`
    percent( n, d, q,   t = 3 )
    percent( n, d,      t = 2 ) 
    percent( n, *, q,   t = 2 )
    percent( q, d,      t = 2 )
    ```
    
    ONE TERM
    --------
    
    "q.q%" if `t` is 1.
    
    ```
    percent( 0.5 )                      # 50%
    percent( 5, 10, t = 1 )             # 50%
    ```
    
    TWO TERMS
    ---------
    
    "n (q.q%)" if `t` if 2 (requires N and D, otherwise uses `t` = 1).

    ```
    percent( 5, 10 )                    # 5 (50%)
    ```
    
    THREE TERMS
    -----------
    
    "n/d (q.q%)" if `t` is 3 (requires N and D, otherwise uses `t` = 1).
    
    ```
    percent( 5, 10, t = 3 )             # 5/10 (50%)
    ```
    
    This is a function for display, hence there are no "division by zero" errors and 0% is
    displayed if both numerator and denominator are zero (if the denominator alone is zero,
    then `"inf%"` is still used).

    :param n:   Specifies the quotient, unless either of `q` or `d` are specified, in which case this parameter specifies the numerator. 
    :param d:   Denominator.
    :param q:   Quotient.
    :param t:   Number of terms to display (1, 2 or 3), if 0 assumes the default for the number of terms provided.
    :param dp:  Decimal places to display for Q.
    
    :exception ValueError:  Q missing or cannot be calculated.
    :exception ValueError:  `t` specified when only Q is known.
    :exception SwitchError: `t` is not 1, 2 or 3.
    """
    fmt = "{{:.{}%}}".format( dp )

    if d is None and ((q is None) != (n is None)):
        # "D" and "Q" missing
        # "N" is actually "Q"
        if q is None:
            q = n

        if (t or 1) != 1:
            raise ValueError(
                f"Cannot specify t = {t} when only `q` is provided. Specified: n={n}, d={d}, q={q}, t={t}, dp={dp}." )

        return fmt.format( q )

    if d is None:
        # "D" missing
        if n is None or q is None:
            raise ValueError( f"Cannot format this percentage. Specified: n={n}, d={d}, q={q}, t={t}, dp={dp}." )

        t = t or 2
        ns = str( n )
        ds = "inf" if q == 0 else str( n / q )
        qs = fmt.format( q )
    elif n is None:
        # "N" missing
        if q is None:
            raise ValueError( f"Cannot format this percentage. Specified: n={n}, d={d}, q={q}, t={t}, dp={dp}." )

        t = t or 2
        ns = "{0:g}".format( q * d )
        ds = str( d )
        qs = fmt.format( q )
    elif q is None:
        # "Q" missing
        t = t or 2
        ns = str( n )
        ds = str( d )
        qs = fmt.format( n / d ) if d != 0 else "0%" if n == 0 else "inf%"
    else:
        # All provided
        t = t or 3
        ns = str( n )
        ds = str( d )
        qs = fmt.format( q )

    if t == 1:
        return "{}".format( qs )
    elif t == 2:
        return "{} ({})".format( ns, qs )
    elif t == 3:
        return "{}/{} ({})".format( ns, ds, qs )
    else:
        from mhelper.exception_helper import SwitchError
        raise SwitchError( "t (terms)", t )


def timedelta_to_string( delta: Union[datetime.timedelta, float], approx=False, hz=False ) -> str:
    """
    Converts a time difference to a human-readable string.
    
    :param delta:       The time difference 
    :param approx:      Returns approximate whole number strings, such as "5
                        minutes" instead of "5:12". 
    :param hz:          Returns times below 1 second in Hz instead of
                        milliseconds/microseconds. 
    """
    if hasattr( delta, "seconds" ):
        s = delta.total_seconds()
    else:
        s = delta

    if math.isinf( s ):
        return str( s )

    if s < 0:
        return "(-{})".format( timedelta_to_string( -s ) )

    if approx:
        if s < 1.0 and hz:
            return "{:,}Hz".format( round( 1 / s ) )

        if s <= 0.010:
            return str( round( s * 1000000 ) ) + " microseconds"

        if s <= 1.5:
            return str( round( s * 1000 ) ) + " milliseconds"

        if s < 60:
            return str( round( s ) ) + " seconds"

        s /= 60

        if s < (60 * 2):
            return str( round( s ) ) + " minutes"

        s /= 60

        if s < 72:
            return str( round( s ) ) + " hours"

        s /= 24

        if s < 14:
            return str( round( s ) ) + " days"

        s /= 7

        if s < 8:
            return str( round( s ) ) + " weeks"

        s /= 4  # an approximation in which we assume 28 day months, i.e. 13 to a year

        if s < 24:
            return str( round( s ) ) + " months"

        s /= 13

        return str( round( s ) ) + " years"

    days = s // 86400
    s -= days * 86400
    hours = s // 3600
    s -= hours * 3600
    minutes = s // 60
    seconds = s - (minutes * 60)

    if days:
        return '%d days, %d:%02d:%02d' % (days, hours, minutes, seconds)
    elif hours:
        return '%d:%02d:%02d' % (hours, minutes, seconds)
    elif minutes or seconds > 1:
        return '%02d:%02d' % (minutes, seconds)
    elif hz:
        return "{:,}Hz".format( round( 1 / seconds ) )
    elif seconds >= 0.010:
        return "{}ms".format( round( seconds * 1000 ) )
    else:
        return "{}μs".format( round( seconds * 1000000 ) )


def fix_width( text: _TStr, width: int = 20, char: _TStr = " ", justify=None, trim=-1, ellipsis: _TStr = "…",
               strip: bool = True, format=None ) -> _TStr:
    """
    Fixes the number of characters in a string.
    
    This function uses `ljust`, `cjust`, `rjust` and `max_width`, so is suitable
    for string-like collections, as well as `str`.
    
    :param text:        Text to fix the width of 
    :param width:       Width to fix to 
    :param char:        Padding character 
    :param justify:     Justify direction (-1, 0, 1). 
    :param ellipsis:    Suffix to add indicating the string has been truncated.
    :param trim:        If the width is excessive, which side of the string to trim (-1, 0, 1).
    :param strip:       Whether to strip and use the first line only.
    :param format:      Formatter (str or callable), see `ljust`.
    """
    if justify is None or justify < 0:
        justify_fn = ljust
    elif justify == 0:
        justify_fn = cjust
    elif justify > 0:
        justify_fn = rjust
    else:
        from mhelper.exception_helper import SwitchError
        raise SwitchError( "justify", justify )

    return justify_fn( max_width( text, width, ellipsis, strip=strip, trim=trim ), width, char, format=format )


def max_width( text: _TStr, width: int = 20, ellipsis: _TStr = "…", prefix: _TStr = "", strip: bool = True,
               trim=-1 ) -> _TStr:
    """
    Limits the number of characters in a string.
    
    This function is suitable for string-like collections, as well as `str`.
    
    :param text:        Text to fix the width of 
    :param width:       Width to fix to 
    :param ellipsis:    Suffix to add indicating the string has been truncated.
    :param prefix:      Prefix to add indicating the string has been truncated. 
    :param strip:       Strip to first line (option).
    :param trim:        Side to trim at (-1 = left, 0 = centre, 1 = right).
    """
    if width < 0:
        raise ValueError( "Invalid width." )

    if width == 0 and text:
        warnings.warn( f"Did you really mean to pass {{width = {width!r}}} to max_width? {{text = {text!r}}}" )

    if strip:
        text = text.strip()
        text = first_line( text )

    if len( text ) > width:
        keep = width - len( ellipsis ) - len( prefix )

        if trim < 0:
            text = text[:keep] + ellipsis
        elif trim > 0:
            text = ellipsis + text[len( text ) - keep:]
        else:
            keep0 = keep // 2
            keep1 = keep0 if keep0 * 2 == keep else keep0 + 1
            text = text[:keep1] + ellipsis + text[len( text ) - keep0:]

        if prefix:
            text = prefix + text

    assert len( text ) <= width
    return text


def format_size( size: int ) -> str:
    """
    Returns a `size`, specified in bytes, as a human-readable string, similar to `ls -h` in bash.
    """
    if size == -1:
        return "?"
    elif size == 0:
        return "0"

    if size < 1024:
        return "{}b".format( size )

    size /= 1024

    if size < 1024:
        return "{0:.1f}kb".format( size )

    size /= 1024

    if size < 1024:
        return "{0:.1f}Mb".format( size )

    size /= 1024

    if size < 1024:
        return "{0:.1f}Gb".format( size )

    size /= 1024

    return "{0:.1f}Tb".format( size )


def is_int( x ) -> bool:
    if not x:
        return False

    try:
        _ = int( x )
        return True
    except Exception:
        return False


def bulk_replace( text, format="<*>", **kwargs ):  # TODO: Specific, deprecate
    for k, v in kwargs.items():
        text = text.replace( format.replace( "*", k ), v )

    return text


__make_name_regex = re.compile( "[^0-9a-zA-Z.]" )


def make_name( name ):  # TODO: Vague
    return __make_name_regex.sub( "_", name )


def strip_lines( text ):
    return __strip_lines_rx.sub( "", text )


def prefix_lines( text, prefix, suffix="" ):
    return prefix + text.replace( "\n", suffix + "\n" + prefix ) + suffix


type_ = type


def type_name( value=None, *, type=None ):
    if type is None:
        type = type_( value )

    if hasattr( type, "__name__" ):  # types or things pretending to be types
        return type.__name__
    else:  # anything else, such as an annotation
        r = type.__str__()

        if r.startswith( "typing." ):
            r = r[7:]

        return r


def undo_camel_case( text: str, sep=" " ):
    """
    Adds spacing to a camel case phrase.
    The case of the result is unaffected.
    
    e.g. "HelloWorld" --> "Hello World" 
    
    :param text: 
    :param sep: 
    :return: 
    """
    result = []

    for i, c in enumerate( text ):
        if i and c.isupper():
            result.append( sep )

        result.append( c )

    return "".join( result )


def name_index( names: List[str], name: Union[str, int] ) -> int:  # TODO: Deprecate - specific use case (CSVs)
    """
    Given a `name`, finds its index in `names`. `name` can be a `str`, an `int` or an int as a str.
    
    :param names: List of names 
    :param name:  Name or index to find 
    :return: Index
    :exception ValueError: Not found
    """
    if isinstance( name, int ):
        index = name
    elif not isinstance( name, str ):
        raise TypeError(
            "`name` should be an `int` or a `str`, but it is «{0}» which is a {1}.".format( name, type_name( name ) ) )
    elif all( str.isdigit( x ) for x in name ):
        return int( name )
    else:
        index = None

    if index is not None:
        if names is not None:
            if not 0 <= index < len( names ):
                raise ValueError(
                    "Trying to find the column with index «{0}» but that is out of range. The columns are: {1}".format(
                        index, names ) )

        return index

    if names is None:
        raise ValueError( "Cannot get columns by name «{0}» when there are no headers.".format( name ) )

    if name in names:
        return names.index( name )

    raise ValueError(
        "Trying to find the column with header «{0}» but that column doesn't exist. The columns are: {1}".format( name,
                                                                                                                  names ) )


def current_time():  # TODO: Deprecate - bad name
    import time
    return time.strftime( "%Y-%m-%d %H:%M:%S %z" )


def ordinal( x: int ) -> str:
    """
    Returns "1st", "2nd", "3rd", etc. from 1, 2, 3, etc.
    `i` can be anything coercible to a string that looks like a number.
    """
    s = str( x )
    e = s[-1]

    if 11 <= x <= 13:
        e = "4"

    if e == "1":
        return s + "st"
    elif e == "2":
        return s + "nd"
    elif e == "3":
        return s + "rd"
    else:
        return s + "th"


def get_indent( line ):
    num_spaces = 0
    for x in line:
        if x == " ":
            num_spaces += 1
        else:
            return num_spaces

    return num_spaces


@overload
def strip_lines_to_first( text: List[str], spaces: str = " " ) -> List[str]:
    pass


@overload
def strip_lines_to_first( text: str, spaces: str = " " ) -> str:
    pass


def strip_lines_to_first( text: Union[List[str], str], spaces: str = " " ) -> Union[str, List[str]]:
    """
    Strips leading spaces from each line to match the indent of the first line.
    
    Leading blank lines are removed.
    Any trailing lines or spaces are removed.
    """
    if not text:
        return ""

    spaces_set = frozenset( spaces )

    if isinstance( text, str ):
        is_list = False
        lines = text.split( "\n" )
    else:
        is_list = True
        lines = text

    first_non_blank = None

    for i, line in enumerate( lines ):
        if line.lstrip( spaces ):
            first_non_blank = i
            break

    if first_non_blank is None:
        return ""

    lines = lines[first_non_blank:]
    first_indent = len( lines[0] ) - len( lines[0].lstrip( spaces ) )

    if first_indent:
        lines = [__remove_indent( first_indent, line, spaces_set ) for line in lines]

    if is_list:
        return lines
    else:
        return "\n".join( lines ).rstrip()


def __remove_indent( current_indent, line: str, spaces=frozenset( " " ) ):
    i = 0

    for i, x in enumerate( line ):
        if x not in spaces:
            break

    i = min( i, current_indent )

    return line[i:]


def capitalise_first_and_fix( text: str, swap="_-", rep=" " ) -> str:
    """
    Takes a variable-name like string, returning a title. 
    """
    text = capitalise_first( text )

    for x in swap:
        text = text.replace( x, rep )

    return text


def capitalise_first( text: str, only=False ) -> str:
    if text is None:
        return ""

    if not text:
        return text

    if len( text ) == 1:
        return text[0].upper()

    if only:
        return text[0].upper() + text[1:].lower()
    else:
        return text[0].upper() + text[1:]


def special_to_symbol( value ):
    return value.replace( "\n", "␊" ).replace( "\r", "␍" ).replace( "\t", "␉" )


def unescape( v ):
    try:
        return v.encode().decode( "unicode_escape" )
    except Exception as ex:
        raise ValueError( "Unescape «{}» failed.".format( v ) ) from ex


DPrint = Callable[[object], None]


class FindError( Exception ):
    pass


def __to_lower( x ):
    return x.lower().replace( ".", "_" ).replace( " ", "_" )


def find( *,
          source: Iterable[object],
          search: str,
          namer: Optional[Union[Callable[[object], str], Callable[[object], Sequence[str]]]] = None,
          detail: Optional[str] = None,
          fuzzy: Optional[bool] = True,
          default=NOT_PROVIDED,
          case: bool = False ):
    """
    Finds the command or plugin with the closest name to "text".
    
    :param case:    Apply case sensitivity and treat non alphanumeric characters differently.
    :param source:  Source list 
    :param search:  Text to find 
    :param namer:   How to translate items in the source list, each item can translate to a `str`, or a `list` or `tuple` of `str` 
    :param detail:  What to call the collection in error messages.
    :param fuzzy:   Permit partial (start-of-word) matches
    :param default: Default to use. If `NOT_PROVIDED` raises an error.
    :return:        The matching item in `source`
    :except FindError: The text was not matched 
    """

    #
    # Arguments
    #
    if not isinstance( source, list ) and not isinstance( source, tuple ):
        source = list( source )

    if not isinstance( search, str ):
        raise TypeError(
            "string_helper.find() takes a `str` and not a {} (`{}`).".format( type( search ).__name__, search ) )

    if namer is None:
        namer = cast( Callable[[object], str], str )

    if not case:
        to_lower = __to_lower
        search = to_lower( search )
    else:
        to_lower = cast( Callable[[str], str], str )

    def __get_names( item ):
        r = namer( item )

        if isinstance( r, str ):
            return [to_lower( r )] if r else []
        elif isinstance( r, list ) or isinstance( r, tuple ):
            return [to_lower( x ) for x in r if x]
        else:
            raise TypeError( "Return value of namer «{}».".format( namer ) )

    #
    # Exact match
    #
    match_items = set()

    for item in source:
        for name in __get_names( item ):
            if search == name:
                match_items.add( item )

    if len( match_items ) == 1:
        return array_helper.single( match_items )

    #
    # Start-of-word match (fuzzy only)
    #
    if fuzzy:
        match_items = set()

        for item in source:
            for name in __get_names( item ):
                if name.startswith( search ):
                    match_items.add( item )

        if len( match_items ) == 1:
            return array_helper.single( match_items )
    else:
        match_items = set()

    #
    # Failure
    #
    if default is not NOT_PROVIDED:
        return default

    if detail is None:
        detail = "item"

    if not match_items:
        ss = []
        ss.append( "No such {}: «{}»".format( detail, search ) )
        available = []

        for item in source:
            for name in __get_names( item ):
                if name:
                    available.append( "'{}' --> {}".format( name, item ) )

        ss.append( "Options: " )
        for option in available[:10]:
            ss.append( "{}".format( option ) )

        if len( available ) > 10:
            ss.append( "(total {} options)".format( len( available ) ) )

        raise FindError( "\n".join( ss ) )

    ss = []
    ss.append( "Ambiguous {} name: «{}»".format( detail, search ) )
    ss.append( "    ...did you mean..." )
    for item in match_items:
        for name in __get_names( item ):
            if search in name:
                ss.append( "    ...... '{}' --> {}".format( name.replace( search, "«" + search + "»" ), item ) )

    raise FindError( "\n".join( ss ) )


def no_emoji( x ):
    return x + "\uFE0E"


def fix_indents( text: str ) -> str:
    text = str( text )
    lines = text.split( "\n" )
    lines[0] = lines[0].lstrip()

    if len( lines ) == 1:
        return lines[0]

    min_leading = 9999

    for line in lines[1:]:
        stripped = line.lstrip()

        if stripped:
            leading = len( line ) - len( stripped )
            min_leading = min( leading, min_leading )

    if min_leading == 9999:
        return text.strip()

    for i in range( 1, len( lines ) ):
        lines[i] = lines[i][min_leading:]

    return "\n".join( lines )


def assert_unicode():
    """
    UTF-8 check. Probably Windows Console Services is badly configured.
    """
    UNICODE_ERROR_MESSAGE = \
        """


        +-------------------------------------------------------------------------------------------------------+--------+
        | UNICODE ENCODE ERROR                                                                                  |        |
        +-------------------------------------------------------------------------------------------------------+  X  X  +
        | It looks like your console doesn't support Unicode.                                                   |        |
        |                                                                                                       |  _--_  |
        | This application needs Unicode to display its UI.                                                     |        |
        | Python doesn't seem to know your terminal doesn't support UTF8 and just crashes :(                    +--------|
        | This problem usually occurs when using cmd.exe on Windows.                                                     |
        |                                                                                                                |
        | On Windows, you could `set PYTHONIOENCODING=ascii:replace` as a quick fix, but it might be better in the long  |
        | run to setup your console and font to support UTF8: https://stackoverflow.com/questions/379240                 |
        |                                                                                                                |
        | On Unix, the quick fix is `export PYTHONIOENCODING=ascii:replace`                                              |
        +----------------------------------------------------------------------------------------------------------------+


        """
    try:
        print( "😁\r \r", end="" )
    except UnicodeEncodeError as ex:
        # On the plus side, Window's Console has a horizontal scroll bar, so we can display an over-sized error message without it breaking...
        raise ValueError( UNICODE_ERROR_MESSAGE ) from ex


def as_delta( value ):
    """
    Returns "+x" or "-x". 
    """
    if value > 0:
        return "+{}".format( value )
    elif value < 0:
        return "{}".format( value )
    else:
        return "±{}".format( value )


def wrap( text: _TStr, width: int = 70, pad: _TStr = None, justify: int = None ) -> Iterator[str]:
    """
    A wrap function that works with string-like collections, as well as `str`.
     
    :param justify:     Justify side.
    :param text:        Text to wrap.
                        This can be a `str` or a `str`-like object such as `AnsiStr`.
                        Only `n = len(text)` and `text[i]` for `i in 0:n` are used, with each `text[i]` always being assumed to have a width of 1.
                        Only `text[i]`'s equality with `" "` and `"\n"` is used to determine spaces and newlines.
    :param width:       Maximum line width 
    :param pad:         When set, all lines are padded to the specified `width` with spaces.
    :return:            An iterator over the lines.
                        A trailing empty line, if present, will not be returned.
    """
    if pad is True:  # old
        pad = type( text )( " " )

    if justify is not None:
        if not pad:
            pad = type( text )( " " )

    if pad:
        pad_fn = lambda x: just( justify, x, width, pad )
    else:
        pad_fn = lambda x: x

    if width <= 0:
        for line in text.split( "\n" ):
            yield line

        return

    text_length = len( text )
    i = 0
    start_line = 0
    last_space = -1
    loop_detector = 0
    max_iter = len( text ) * 10

    while i < text_length:
        loop_detector += 1

        if loop_detector > max_iter:
            raise ValueError(
                "Infinite loop when trying to parse text. Loops = {}, text length = «{}», width = «{}», padding = «{}».".format(
                    loop_detector, len( text ), width, pad ) )

        c = text[i]

        if c == " " or c == "\n":
            if (i - start_line) < width:
                if c == " ":
                    # Still enough space, continue adding
                    last_space = i
                else:  # c == "\n"
                    # Still enough space, print newline now
                    yield pad_fn( text[start_line:i] )
                    start_line = i + 1
                    last_space = start_line

                    # No more room
        if (i - start_line) >= width:
            if start_line != last_space + 1:
                # Backtrack to last space
                i = last_space
                yield pad_fn( text[start_line:i] )
                start_line = i + 1  # skip over space
            else:
                # Cannot backtrack to last space, just take as much as possible
                i = start_line + width
                yield pad_fn( text[start_line:i] )
                start_line = i
                last_space = start_line

        i += 1

    if i != start_line:
        final = text[start_line:i]

        if final.strip():
            yield pad_fn( final )


def just( side: int, text: _TStr, width: int, char: _TStr ) -> _TStr:
    """
    An justify function that works with string-like collections, as well as
     `str`.
    """
    if side < 0:
        return ljust( text, width, char )
    elif side == 0:
        return cjust( text, width, char )
    else:
        return rjust( text, width, char )


def __format( text, format ):
    if format is None:
        return text

    if isinstance( format, str ):
        return format.format( text )
    else:
        return format( text )


def ljust( text: _TStr, width: int, char: _TStr, format=None ) -> _TStr:
    """
    An `ljust` function that works with string-like collections, as well as
     `str`.
     
    :param text:        Text to justify 
    :param width:       Width to justify into 
    :param char:        Character to pad with 
    :param format:      Formatting, applied *before* the padding but after the 
                        padding required has been determined. Used to insert
                        formatting/markup around the text but not around the
                        padding. This may be a str (containing `"{}"`) or a
                        callable, accepting a `str` and returning a `str`. 
    :return: 
    """
    needed = width - len( text )
    text = __format( text, format )

    if needed <= 0:
        return text

    return text + char * needed


def rjust( text: _TStr, width: int, char: _TStr, format=None ) -> _TStr:
    """
    An `rjust` function that works with string-like collections, as well as 
    `str`. Takes the same parameters as `ljust`.
    """
    needed = width - len( text )
    text = __format( text, format )

    if needed <= 0:
        return text

    return char * needed + text


def cjust( text: str, width: int, char: str = " ", format=None ) -> str:
    """
    An `center` function that works with string-like collections, as well as 
    `str`. Takes the same parameters as `ljust`.
    """
    needed = width - len( text )

    if needed <= 0:
        return text

    text = (char * (needed // 2)) + text
    text = ljust( text, width, char, format )
    return text


def bracketed_split( text: str, split: str, start: str, end: str ) -> List[str]:
    """
    Splits a string about a delimiter, accounting for quotes.
    
    :param text:    Input text 
    :param split:   Delimiter character 
    :param start:   Start quote character
    :param end:     End quote character
    """
    inside = False
    r = []
    cur = []
    no_more = False
    no_br = False
    ebr = 0

    for c in text:
        if inside:
            if c in end:
                ebr -= 1

                if ebr >= 0:
                    cur.append( c )
                else:
                    inside = False
                    no_more = True
            elif c in start:
                ebr += 1
                cur.append( c )
            else:
                cur.append( c )
        else:
            if c in start and not no_br:
                inside = True
            elif c in split:
                no_br = False
                no_more = False
                ebr = 0
                r.append( "".join( cur ) )
                cur.clear()
            elif c.isspace():
                if no_more:
                    continue
                elif no_br:
                    cur.append( c )
            else:
                if no_more:
                    raise ValueError( "Malformed string: {}".format( repr( text ) ) )

                cur.append( c )
                no_br = True

    r.append( "".join( cur ) )

    return r


def split_strip( x: str, y: str, z: int ) -> List[str]:
    """
    As `str.split`, but `str.strip`\s the results.
    """
    return [v.strip() for v in x.split( y, z )]


def shrink_space( x: str ) -> str:
    """
    Replaces concurrent spaces with a single space.
    """
    return __shrink_space_rx.sub( " ", x )


class StringBuilder:
    class Line:
        def __init__( self, sb ):
            self.sb = sb

        def __call__( self, *args, **kwargs ):
            return self.sb( *args, **kwargs, _replace=True )

    def __init__( self, *, end="\n" ):
        self.content = []
        self.end = end
        self.line = self.Line( self )

    def __call__( self, text, *args, end=None, _replace=False, **kwargs ) -> Callable:
        if _replace:
            del self.content[-1]

        text = str( text )

        if not args and not kwargs:
            self.content.append( text )
        else:
            self.content.append( text.format( *args, **kwargs ) )

        if end is None:
            end = self.end

        if end:
            self.content.append( end )
            return self.line
        else:
            return self

    def __str__( self ):
        return "".join( self.content )


def object_to_string( v: _TSimple ) -> str:
    """
    Converts an object of an inbuilt type (str, int, float, bool, Enum, Flag) to a string.
    """
    if isinstance( v, str ) or isinstance( v, int ) or isinstance( v, float ):
        return str( v )
    elif isinstance( v, Flag ):
        return flag_to_string( v )
    elif isinstance( v, Enum ):
        return enum_to_string( v )
    else:
        from mhelper.exception_helper import SwitchError
        raise SwitchError( "object_to_string::v", v, instance=True )


def string_to_object( t: Type[_TSimple], v: str ) -> _TSimple:
    """
    Converts a string to an object of an inbuilt type (str, int, float, bool, Enum, Flag).
    """
    if t is str:
        return v
    elif t is bool:
        return string_to_bool( v )
    elif t is int:
        return int( v )
    elif t is float:
        return float( v )
    elif issubclass( t, Flag ):
        return string_to_flag( t, v )
    elif issubclass( t, Enum ):
        return string_to_enum( t, v )
    else:
        from mhelper.exception_helper import SwitchError
        raise SwitchError( "string_to_object::t", t )


def enum_to_string( v: _TEnum ) -> str:
    """
    Returns the human-readable name of the enum, without the class.
    
    .. note::
    
        `str(Enum())` is more like what we'd expect from `repr(Enum())` and
        includes the class, `repr(Enum())` actually gives something else.
    """
    return v.name


def enum_to_repr( v: _TEnum ) -> str:
    """
    Returns the Python representation of an enum.
    
    .. note::
    
        For reasons only known to the creators, `repr(Enum())` gives a weird
        answer that Python doesn't understand. 
    """
    return str( v )


def flag_to_string( v: Flag, delimiter: str = "|" ) -> str:
    r = []

    for fk, fv in type( v ).__members__.items():
        if fv and fv in v:
            r.append( fk )

    return array_to_string( r, delimiter )


def mask_to_string( v: int, delimiter: str = "|", fn: Union[str, Callable[[int], str]] = "d" ) -> str:
    """
    Splits the values of a mask and returns them as a concatenated string.
    
    :param v:   The value, e.g. `12`
    :param delimiter: Delimiter, e.g. `"|"`
    :param fn:      `"s"`    --> As shifts,  e.g. `"1<<2|1<<3"`
                    `"d"`    --> As decimal, e.g. `"4|8"`
                    `"b"`    --> As binary,  e.g. `"100|1000"`
                    `"x"`    --> As hex,     e.g. `"4|8"`
                    `object` --> Use call,   e.g. `"fn(4)|fn(8)"`  
    :return: String representation
    """
    s = "{0:b}".format( v )

    if fn == "s":
        fn = lambda x: "1<<{}".format( x )
    elif fn == "d":
        fn = lambda x: 2 ** x
    elif fn == "b":
        fn = lambda x: "{0:b}".format( 2 ** x )
    elif fn == "x":
        fn = lambda x: "{0:x}".format( 2 ** x )

    r = []

    for i, c in enumerate( reversed( s ) ):
        if c == "1":
            r.append( fn( i ) )

    return array_to_string( r, delimiter )


def string_to_enum( t: Type[_TEnum], v: str, default=NOT_PROVIDED, ignore_case=True ) -> _TEnum:
    """
    Converts a string to an enum.
    
    Handles enum member aliases and is case insensitive by default. 
    """
    try:
        try:
            return t[v]  # Enum name
        except KeyError as ex:
            if ignore_case:
                lower_to_actual = {x.lower(): x for x in dir( t )}
                v = lower_to_actual.get( v.lower(), v )

            # Failed mapping - try getattr to see if it's an alias
            r = getattr( t, v, None )

            if not isinstance( r, t ):
                from mhelper import exception_helper
                raise exception_helper.type_error( "retrieved_value", r, t ) from ex  # trapped below

            return r
    except Exception as ex:
        if default is NOT_PROVIDED:
            avail = ", ".join( x.name for x in t )
            raise ValueError(
                f"Cannot convert string {v!r} to enum type {t.__name__!r}. The available options are: {avail}" ) from ex
        else:
            return default


def string_to_flag( t: Type[_TFlag], v: str, delimiter: str = "|", default=NOT_PROVIDED ) -> _TFlag:
    for d2 in delimiter[1:]:
        v = v.replace( delimiter[0], d2 )

    e = v.split( delimiter[0] )
    r = t( 0 )
    pfx = t.__name__ + "."

    for ee in e:
        try:
            if ee.startswith( pfx ):
                ee = ee[len( pfx ):]

            if ee.isdigit():
                r |= t( int( ee ) )
            else:
                r |= t[ee]
        except Exception as ex:
            if default is NOT_PROVIDED:
                raise ValueError(
                    "Cannot convert the string {}, specifically the part that reads {}, to the flag type `{}`.".format(
                        repr( v ), repr( ee ), t.__name__ ) ) from ex
            else:
                return default

    return r


_range = range
_cast = cast


def string_to_list( cast: Callable[[str], _T],
                    text: str,
                    delimiter: str = ",",
                    ignore_empty: bool = False,
                    range: Union[None, str, bool] = None,
                    range_cast: Optional[Callable[[int], _U]] = None
                    ) -> List[Union[_T, _U]]:
    """
    Converts a string to a list.
    
    :param cast:            Type of values in the resulting list. 
    :param text:            Input text. 
    :param delimiter:       Delimiter on values. 
    :param ignore_empty:    Do not include empty values in the list. 
    :param range:           When truthy, allows specifying inclusive ranges such 
                            as ``"10-12"`` (10, 11, 12).
                            If this is a `str` it is used as the range
                            delimiter, replacing "``-``".
                            The default, `None` assumes `True` if `cast` is 
                            `int`, otherwise `False`.
    :param range_cast:      Type to cast `range` values into. The default, 
                            `None` assumes the same as `cast`. Note that this
                            implies that `cast` must also accept `int`.
    :return:                List.
    """
    if not text:
        return []

    if range is None:
        range = True if cast is int else False

    if range_cast is None:
        range_cast = _cast( Callable[[int], _T], cast )

    if range:
        if range is True:
            range = "-"

        r = []

        for element in text.split( delimiter ):
            if range in element:
                s, e = element.split( range, 1 )
                r.extend( range_cast( z ) for z in _range( int( s ), int( e ) + 1 ) )
            elif not ignore_empty or element:
                r.append( cast( element ) )

        return r

    if ignore_empty:
        return [cast( element ) for element in text.split( delimiter ) if element]
    else:
        return [cast( element ) for element in text.split( delimiter )]


__string_to_bool_true = {"true", "yes", "t", "y", "1", "on"}
__string_to_bool_false = {"false", "no", "f", "n", "0", "off"}


def string_to_bool( x: str, default: bool = NOT_PROVIDED ) -> bool:
    """
    Converts a string to a boolean value, accepting several variations of "yes"
    and "no".
    :param x:           Text 
    :param default:     Used if the string is empty or nonsensical. The default
                        is to raise an error. 
    :return:            Result or default.
    """
    x = x.lower()
    if x in __string_to_bool_true:
        return True
    elif x in __string_to_bool_false:
        return False
    elif default is NOT_PROVIDED:
        raise ValueError( "Cannot convert «{}» to boolean.".format( x ) )
    else:
        return default


def string_to_int( x: str, default=None ) -> Optional[int]:
    return string_to_t( int, x, default )


def string_to_float( x: str, default=None ) -> Optional[int]:
    return string_to_t( float, x, default )


def string_to_t( t: Type[_T], x: str, default: Optional[_T] = NOT_PROVIDED ) -> Optional[_T]:
    """
    Converts a string to the specified type. Special handlers are in place for
    boolean, flag and enum values.
    
    :param t:       Destination type
    :param x:       Text 
    :param default: Value to use if the string is empty or nonsensical.
    :return:        Result or default.
    """
    if not x:
        return default

    if t is bool:
        return string_to_bool( x, default )
    elif issubclass( t, Flag ):
        return string_to_flag( t, x, default=default )
    elif issubclass( t, Enum ):
        return string_to_enum( t, x, default )

    try:
        return t( x )
    except Exception:
        if default is NOT_PROVIDED:
            raise ValueError( "Cannot convert {} to {}.".format( repr( x ), t.__name__ ) )
        else:
            return default


def counter_to_str( counter: Dict[object, int], delimiter: str = ", ", format="{count} × {value}" ) -> str:
    """
    Converts a counter to a string.
    
    :param counter:     Counter or dictionary. 
    :param delimiter:   Array delimiter.
    :param format:      Item format. 
    :return:            Text.
    """
    r = []

    if "{count}" not in format and "{value}" not in format:
        format = "{count}" + format + "{value}"

    for k, v in sorted( counter.items(), key=lambda x: -x[1] ):
        r.append( format.format( count=v, value=k ) )

    return delimiter.join( r )


def array_to_string( array: Iterable,
                     delimiter: str = ", ",
                     last_delimiter: str = None,
                     sort: Optional[bool] = None,
                     format: FormatDelegate = None,
                     limit: int = None,
                     ellipsis: str = "...",
                     empty: str = "∅",
                     autorange: bool = False,
                     qualifiers: Tuple[str, str] = None,
                     join=None ) -> str:
    """
    Converts an array to a string.
    
    :param autorange:       Create ranges such as "4-8" from text.
    :param array:           The array (any iterable) 
    :param delimiter:       How to join 
    :param last_delimiter:  How to join the final element (e.g. "``and``").
                            The default, `None`, uses the `delimiter`. 
    :param sort:            Whether to sort.
                            The default, `None` assumes `False` unless `array` is a `set`. 
    :param format:          How to format the text, e.g. `my_function` or `"blah{}blah".format` 
    :param limit:           Limit to this many items.
    :param ellipsis:        Denote "max" items with this symbol
    :param empty:           Returned for empty array
    :param qualifiers:      Optional tuples of suffixes to the string - the first suffix is the
                            singular suffix, the second is the plural. If the array is empty no
                            suffix is added (use `empty` to specify this instead).
    :param join:            Method used to concatenate the final string, defaults to ``"".join``.
    :return:                String representation of the array
    """
    if array is None:
        return empty

    if limit is None:
        limit = -1

    format = __format_to_fn( format )

    if sort is None:
        sort = isinstance( array, set )

    if autorange:
        copy = list( array )
        array = []
        prefix_to_numbers = defaultdict( list )

        i = len( copy ) - 1

        while i >= 0:
            item = copy[i]
            item_str = format( item )
            elements = re.split( "([0-9]+)", item_str, 1 )

            if len( elements ) == 3:
                prefix_to_numbers[(elements[0], elements[2])].append( int( elements[1] ) )
            else:
                array.append( item_str )

            i -= 1

        for (prefix, suffix), numbers in prefix_to_numbers.items():
            for start, end in array_helper.get_ranges( numbers ):
                if start == end:
                    array.append( prefix + str( start ) + suffix )
                else:
                    array.append( prefix + str( start ) + "-" + str( end ) + suffix )

        format = str

    if sort:
        array = sorted( array, key=format )

    if last_delimiter is None and limit == -1 and not empty and not qualifiers and join is None:
        return delimiter.join( format( x ) for x in array )
    else:
        if join is None:
            join = "".join

        if last_delimiter is None:
            last_delimiter = delimiter

        r = []

        for index, (item, is_first, is_last) in enumerate( array_helper.when_first_or_last( array ) ):
            if index == limit:
                r.append( delimiter )
                r.append( ellipsis )
                break

            if not is_first:
                if is_last or index == limit - 1:
                    r.append( last_delimiter )
                else:
                    r.append( delimiter )

            r.append( format( item ) )

        if not r:
            return empty

        if qualifiers:
            if index:
                r.append( qualifiers[1] )  # plural
            else:
                r.append( qualifiers[0] )  # singular

        return join( r )


def __format_to_fn( format ):
    if format is None:
        format = str
    elif isinstance( format, str ):
        format = (lambda y: lambda x: y.format( x ))( format )
    return format


def string_to_hash( x: str, *, encoding="utf-8", hash=None, binary=False ):
    if hash is None:
        import hashlib
        hasher = hashlib.sha256()
    elif isinstance( hash, str ):
        import hashlib
        hasher = getattr( hashlib, hash )()
    else:
        hasher = hash

    hasher.update( x.encode( encoding ) )
    if binary:
        return hasher.digest()
    else:
        return hasher.hexdigest()


# region Deprecated

def remove_prefix( text, prefix ) -> str:
    warnings.warn( "Deprecated - use curtail", DeprecationWarning )
    return curtail( text, prefix )


def to_int( *args, **kwargs ):
    warnings.warn( "Deprecated. Use `string_to_int`.", DeprecationWarning )
    return string_to_int( *args, **kwargs )


def to_bool( *args, **kwargs ):
    warnings.warn( "Deprecated. Use `string_to_bool`.", DeprecationWarning )
    return string_to_bool( *args, **kwargs )


def format_array( array: Iterable,
                  join: str = ", ",
                  final: str = None,
                  sort: Optional[bool] = None,
                  format: Union[str, Callable[[object], str]] = str,
                  limit: int = -1,
                  limit_symbol: str = "...",
                  empty: str = "∅",
                  autorange: bool = False
                  ) -> str:
    warnings.warn( "Deprecated. Use `array_to_string`", DeprecationWarning )
    return array_to_string( array=array,
                            delimiter=join,
                            last_delimiter=final,
                            sort=sort,
                            format=format,
                            limit=limit,
                            ellipsis=limit_symbol,
                            empty=empty,
                            autorange=autorange )


def join_ex( sequence: Iterable[object], delimiter=", ", last_delimiter=None, formatter=None ) -> str:
    """
    Join, with more functionality.
    
    :param sequence:            Sequence to join, can be any type. 
    :param delimiter:           Delimiter 
    :param last_delimiter:      Delimiter before the final item (e.g. `" and "` or `" or "`). `None` is the same as `delimiter. 
    :param formatter:           Formatter function, such as `str`, or a format string, such as `"{}"`. `None` defaults to `str`.
    :return:                    Joined string. 
    """
    warnings.warn( "Deprecated. Use `array_to_string`", DeprecationWarning )
    return array_to_string( array=sequence,
                            delimiter=delimiter,
                            last_delimiter=last_delimiter,
                            format=formatter,
                            empty="" )


def summarised_join( source: Counter, delimiter ) -> str:
    warnings.warn( "Deprecated.", DeprecationWarning )
    return counter_to_str( source, delimiter )


class EnumMap:  # TODO: Specific, deprecate
    def __init__( self ):
        warnings.warn( "Deprecated - too specific", DeprecationWarning )
        self.__to_names = {}
        self.__to_value = {}

    def __call__( self, value, *names ):
        names = tuple( x.lower() for x in names )

        self.__to_names[value] = names

        for name in names:
            self.__to_value[name] = value

        return value

    def to_name( self, value: int, default=None ) -> str:
        return self.__to_names.get( value, [default] )[0]

    def to_value( self, string: str, default=None ) -> int:
        return self.__to_value.get( string.lower(), default )


def time_now() -> str:
    warnings.warn( "Deprecated - use current_time()", DeprecationWarning )
    t = datetime.datetime.now()
    return t.strftime( '%Y-%m-%d %H:%M:%S' )


def time_to_string( time: float ) -> str:
    warnings.warn( "Deprecated - timedelta_to_string", DeprecationWarning )
    return timedelta_to_string( time, approx=True )


def time_to_string_short( time: float, delimiter: str = ":" ) -> str:
    warnings.warn( "Deprecated - timedelta_to_string", DeprecationWarning )

    SECONDS_IN_ONE_HOUR = 60 * 60
    SECONDS_IN_ONE_MINUTE = 60

    hours = time // SECONDS_IN_ONE_HOUR
    time -= hours * SECONDS_IN_ONE_HOUR

    minutes = time // SECONDS_IN_ONE_MINUTE
    time -= minutes * SECONDS_IN_ONE_MINUTE

    seconds = time

    h_text = ""

    if hours:
        h_text = str( int( hours ) ) + delimiter

    m_text = str( int( minutes ) ).rjust( 2, "0" ) + delimiter

    s_text = str( int( seconds ) ).rjust( 2, "0" )

    return h_text + m_text + s_text


# endregion

def merge( *sequence: Iterable[Optional[object]], delimiter: str = "" ):
    """
    Performs a `delimiter.join` of non-null elements of the sequence, as strings.
    """
    return delimiter.join( str( x ) for x in sequence if x is not None )


def constrain_chars( input: str, permitted="aA0", replace="_" ):
    r = []
    v = False

    permitted = permitted.replace( "a", "abcdefghijklmnopqrstuvwxyz" )
    permitted = permitted.replace( "A", "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
    permitted = permitted.replace( "0", "0123456789" )

    for c in input:
        if c in permitted:
            r.append( c )
            v = True
        else:
            if v:
                r.append( replace )
                v = False

    return "".join( r ).rstrip( replace )


def make_variable_name( input: str, in_use: Set[str] = None ):
    if not input:
        input = "V"
    elif input.isdigit():
        input = "V{}".format( input )

    input = constrain_chars( input )

    if input[0].isdigit():
        input = "_" + input

    if in_use is not None:
        orig = input
        n = 2

        while input in in_use:
            input = "{}_{}".format( orig, n )
            n += 1

        in_use.add( input )

    return input


_wrap = wrap


def format_row( data, widths, wrap=False, left="| ", centre=" | ", right=" |", line="\n" ):
    if wrap:
        data = [_wrap( d, w ) for d, w in zip( data, widths )]
    else:
        data = [[max_width( d, w )] for d, w in zip( data, widths )]

    r = []

    for row_index, row in enumerate( zip_longest( *data, fillvalue="" ) ):
        if row_index != 0:
            r.append( line )

        r.append( left )

        for col_index, col, width in zip( count(), row, widths ):
            if col_index != 0:
                r.append( centre )

            r.append( fix_width( col, width ) )

        r.append( right )

    return "".join( r )


# region Deprecated

def first_words( t: str, min_length=1 ) -> str:
    """
    DEPRECATED (weird specific case)
    
    Returns a string made up of the first and last words (optionally allows a min_length of first words)
    """
    warnings.warn( "Deprecated. Please use custom implementation.", DeprecationWarning )
    result = ""
    last_iter = ""
    for match in re.finditer( r"[\w]+", t ):
        if len( match.group( 0 ) ) <= 1:
            continue

        last_iter = match.group( 0 )

        if len( result ) < min_length:
            if result:
                result += " "
            result += last_iter
            last_iter = None
    if result:
        if last_iter:
            return result + " " + last_iter
        else:
            return result
    else:
        return t


def first_word( t: str ) -> str:
    """
    DEPRECATED (weird specific case)
    
    Returns the first word from the string
    """
    warnings.warn( "Deprecated. Please use custom implementation.", DeprecationWarning )

    match = re.match( r"[\w]+", t )

    if not match:
        return t

    return match.group( 0 )


def highlight_words( text: str, words, colour, normal ):
    """
    DEPRECATED
    """
    warnings.warn( "This doesn't work properly and has been deprecated", DeprecationWarning )

    text = normal + text

    for x in words:
        text = highlight_regex( text, "/\b($" + x + ")\b/i", colour, normal )

    return text


def percent( *args, **kwargs ) -> str:
    """
    DEPRECATED
    """
    warnings.warn( "Deprecated - use percent_to_string", DeprecationWarning )
    return percent_to_string( *args, **kwargs )


def first_line( text: str ) -> str:
    """
    Returns the first line of a text block.
    """
    if "\n" in text:
        text = text[:text.index( "\n" )]

    return text


def centre_align( text, width, char=" ", prefix=None, suffix=None ):
    """
    DEPRECATED
    
    Centre aligns text.
    
    :param suffix:  Prefix to use in output. e.g. colour codes that shouldn't be considered as part of the length.
    :param prefix:  Suffix to use in output. e.g. colour codes that shouldn't be considered as part of the length.
    :param text:    Text to align 
    :param width:   Width to align into 
    :param char:    Padding character
    :return:        Aligned text. 
    """
    warnings.warn( "Deprecated - use cjust.", DeprecationWarning )

    use = text

    if prefix:
        use = prefix + use

    if suffix:
        use += suffix

    length = len( text )

    pad_len = (width - length) // 2 - 1
    pad = char * pad_len

    if (length % 2) != 0 and (length + pad_len * 2) < width:
        return pad + use + pad + char
    else:
        return pad + use + pad


# endregion
__random_text_map = {"A": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "a": "abcdefghijklmnopqrstuvwxyz",
                     "0": "0123456789",
                     "Z": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                     "z": "abcdefghijklmnopqrstuvwxyz0123456789",
                     "x": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"}


def get_random_text( format ):
    """
    Obtains random text.
    
    :param format:      A = any upper case
                        a = any lower case
                        0 = any digit
                        Z = any upper case or digit
                        z = any lower case or digit
                        x = any upper case or lower case or digit
                        all other alphanumeric = undefined
                        all symbols = verbatim
    :return: 
    """
    r = []

    for c in format:
        cs = __random_text_map.get( c )

        if cs:
            r.append( random.choice( cs ) )
        else:
            r.append( c )

    return "".join( r )


def get_random_varname( len=8, char_set: str = "a" ):
    if char_set == "a":
        char_set = "abcdefghijklmnopqrstuvwxyz"
    elif char_set == "A":
        char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif char_set == "a0":
        char_set = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif char_set == "A0":
        char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif char_set == "0":
        char_set = "0123456789"
    elif char_set.__len__() == 1:
        raise ValueError( "Invalid char_set." )

    return "".join( random.choice( char_set ) for _ in range( len ) )


def get_random_alphanumeric( len=8 ):
    return get_random_varname( len, char_set="A0" )


def array_and_dict_to_string( array: Iterable,
                              dictionary: dict,
                              delimiter: str = ", ",
                              last_delimiter: str = None,
                              format: Union[str, Callable[[object], str]] = None,
                              value_format: Union[str, Callable[[object], str]] = None,
                              key_format: Union[str, Callable[[object], str]] = None,
                              kv_format: Union[str, Callable[[object, object], str]] = None,
                              limit: int = None,
                              ellipsis: str = "...",
                              empty: str = "∅" ) -> str:
    if format is not None:
        key_format = format
        value_format = format

    value_format = __format_to_fn( value_format )
    key_format = __format_to_fn( key_format )

    if kv_format is None:
        kv_format = lambda x1, x2: "{}={}".format( key_format( x1 ), value_format( x2 ) )
    elif isinstance( kv_format, str ):
        kv_format_str = kv_format
        kv_format = lambda x1, x2: kv_format_str.format( key_format( x1 ), value_format( x2 ) )

    r = itertools.chain( (value_format( v ) for v in array),
                         (kv_format( k, v ) for k, v in dictionary.items()) )
    return array_to_string( array=r,
                            delimiter=delimiter,
                            last_delimiter=last_delimiter,
                            limit=limit,
                            ellipsis=ellipsis,
                            empty=empty )


def dict_to_string( dict_: dict, empty: str = "" ):
    return array_to_string( array=(f"{k} = {v!r}" for k, v in dict_.items()),
                            delimiter=", ",
                            empty=empty )


def try_str( x, default="STR_ERROR" ):
    """
    Tries to coerce x to a str, or returns a default on failure.
    """
    try:
        return str( x )
    except Exception:
        return default


def abbreviate( txt, w, delim=" " ):
    if len( delim ) > 1:
        td = delim[0]

        for d in delim[1:]:
            txt = txt.replace( d, td )

        delim = td

    e = txt.split( delim )
    spe = w / len( e )

    if spe < 1:
        return "".join( e[i][0] for i in range( w ) )
    else:
        spe = int( spe )
        return "".join( x[:spe] for x in e )


def bullet( bullet: str, text: str ):
    return bullet + indent( text, len( bullet ), first=False )


def indent( text: str, w: int = 4, char: str = " ", first: bool = True ) -> str:
    lines = text.split( "\n" )
    indent_ = char * w

    if first:
        return "\n".join( indent_ + line for line in lines )
    else:
        return ("\n" + indent_).join( lines )


def code_repr( x: Any ) -> str:
    """
    This exists because Mypy treats a property as a *property*, which causes an
    error when trying to reflect upon the *descriptor*, otherwise `x.fget.__name__`
    is probably more concise than `string_helper.code( x )`.
    """
    if isinstance( x, type ):
        return x.__qualname__
    elif isinstance( x, property ):
        return x.fget.__qualname__
    else:
        raise ValueError( f"Cannot determine code for {x}." )


def format_delegate( format: FormatDelegate, value: object ) -> str:
    """
    Uses `format` to format `value`, accepting any type from the
    `FormatDelegate` union.
    
    * `str` - is a format string containing ``{}``.
    * `callable` - is a format function
    * `None`/`Type[str]` - use `__str__`. 
    """
    if format is None:
        return str( value )
    elif isinstance( format, str ):
        return format.format( value )
    else:
        return format( value )


def hard_wrap_iter( text, width: int ) -> Iterable[str]:
    for s in range( 0, len( text ), width ):
        next = text[s:s + width]

        for n in next.split( "\n" ):
            yield n


def hard_wrap( *args, **kwargs ) -> str:
    return "\n".join( hard_wrap_iter( *args, **kwargs ) )


def repr_html( obj ):
    """
    Uses `_repr_html_` or `__str__` on `obj`.
    
    (The naming convention comes from Jupyter) 
    """
    _repr_html_ = getattr( obj, "_repr_html_", None )

    if _repr_html_ is not None:
        return _repr_html_()

    return str( obj )


def auto_repr( *args, **kwargs ) -> str:
    """
    Alias of `mhelper.debug_helper.dump_repr`
    
    Intended as a quick solution to __repr__
    """
    from mhelper.debug_helper import dump_repr
    return dump_repr( *args, **kwargs )


class AutoRepr:
    def __repr__( self ):
        return auto_repr( self )


class AutoReprMixin:
    def __repr__( self ):
        return auto_repr( self )


def place_into( source, dest, wildcard="?" ):
    """
    Places another string into the destination, a character at a time.
    
    :param source:      Source text, e.g. "hello_world" 
    :param dest:        Destination format, e.g. "????-????" 
    :param wildcard:    Wildcard character, e.g. "?" 
    :return:            Formatted dest, e.g. "hell-o_wo" 
    """
    r = []

    it = iter( source )

    for char in dest:
        if char == wildcard:
            try:
                r.append( next( it ) )
            except StopIteration:
                break
        else:
            r.append( char )

    return "".join( r )


def replace_env( text: str ) -> str:
    import os
    return replace_all( text, os.environ, "${{{}}}" )


def replace_all( text, replacements, tkey=None, tvalue=None ):
    """
    :param text:            Source text         
    :param replacements:    Dictionary or iterable of tuples 
    :param tkey:            Transformation on key, as str format or callable 
    :param tvalue:          Transformation on value, as str format or callable
    :return:                Text 
    """
    if hasattr( replacements, "items" ):
        replacements = replacements.items()

    if isinstance( tkey, str ):
        tkey = tkey.format

    if isinstance( tvalue, str ):
        tvalue = tvalue.format

    for key, value in replacements:
        if tkey:
            key = tkey( key )

        if tvalue:
            value = tvalue( value )

        text = text.replace( key, value )

    return text


def normalise( text: str,
               transform: Callable[[str], str] = str.lower,
               condition: Callable[[str], bool] = str.isalnum
               ) -> str:
    """
    Lower case and ignore non alphanumeric characters.
    """
    return "".join( transform( x ) for x in text if condition( x ) )


def indent_value( text: str, assignment="=", char=" " ):
    """
    Indents the "value" of text, for instance:
    
        name = a value
        with multiple
        lines.
        
    Becomes:
    
        name = a value
               with multiple
               lines.
        
        
    :param text:            Input text 
    :param assignment:      Assignment character. 
    :param char:            Spacing character. 
    :return:                Formatted text. 
    """
    indent = text.find( assignment )

    if not indent:
        raise ValueError( "Text must contain the assignment." )

    indent += len( assignment )

    while text[indent].isspace():
        indent += 1

    indent_text = char * indent
    lines = text.split( "\n" )
    lines = [lines[0], *(indent_text + line for line in lines[1:])]
    return "\n".join( lines )


def contains_pointers( x ):
    return bool( re.search( r"at 0x[0-9]+", x ))
