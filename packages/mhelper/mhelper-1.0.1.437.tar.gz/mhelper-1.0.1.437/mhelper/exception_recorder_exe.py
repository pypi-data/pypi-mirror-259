import sys
import functools
import os
from dataclasses import dataclass
from typing import List, Optional, Callable, Set
from mhelper.exception_formatter import EStyle, format_traceback as _format_traceback, EFormat as _EFormat
from mhelper import string_helper
from mhelper import exception_recorder

def _main():
    """
    Display error logs.
    """
    import datetime
    import os
    import argparse
    from mhelper import io_helper
    import pydoc

    # Arguments
    p = argparse.ArgumentParser()
    p.add_argument( "dir", help = "Directory to read from" )
    p.add_argument( "id", help = "Name or index to read."
                                 "'list' to list items."
                                 "'first' to show the earliest entry."
                                 "'last' to show the latest entry."
                                 "'review' to show the earliest unread entry." )

    p.add_argument( "--read", "-r", action = "store_true", help = "Select the list of only read items" )
    p.add_argument( "--unread", "-u", action = "store_true", help = "Select the list of only unread items" )

    p.add_argument( "--pager", "-p", action = "store_true", help = "Use the pager" )
    p.add_argument( "--const", action = "store_true", help = "Read without marking as read" )
    p.add_argument( "--mark", "-M", action = "store_true", help = "Mark all as read" )
    p.add_argument( "--unmark", "-U", action = "store_true", help = "Mark all as unread" )

    p.add_argument( "--dir", action = "store", help = "Use this directory" )

    a = p.parse_args().__dict__

    dir_ = a["dir"]
    arg_id = a["id"]
    arg_read = a["read"]
    arg_unread = a["unread"]
    arg_pager = a["pager"]
    arg_const = a["const"]
    arg_mark = a["mark"]
    arg_unmark = a["unmark"]

    # List the files and read-list
    print( f"DIRECTORY: {dir_}" )
    extension: str = ".ansi"
    list_all: List[str] = [os.path.join( dir_, fn ) for fn in os.listdir( dir_ ) if fn.endswith( extension )]
    history_path: str = os.path.join( dir_, "readlist.txt" )
    set_read_bn: Set[str] = set( io_helper.read_all_lines( history_path ) if os.path.isfile( history_path ) else () )
    list_all = sorted( list_all, key = lambda fn: os.path.getctime( fn ) )
    list_read: List[str] = [x for x in list_all if os.path.basename( x ) not in set_read_bn]
    list_unread: List[str] = [x for x in list_all if os.path.basename( x ) in set_read_bn]

    # Select the focus
    if arg_read:
        print( f"SELECTING READ ENTRIES ONLY: {len( list_unread )}" )
        focus = list_unread
    elif arg_unread:
        print( f"SELECTING UNREAD ENTRIES ONLY: {len( list_read )}" )
        focus = list_read
    else:
        print( f"SELECTING ALL ENTRIES: {len( list_all )}" )
        focus = list_all

    print( f"{len( list_read )} UNREAD, {len( list_unread )} READ, {len( list_all )} TOTAL." )

    focus_: List[str] = sorted( focus, key = lambda fn: os.path.getctime( fn ) )

    if arg_id == "list":
        # List all the items
        for i, fn in enumerate( focus_ ):
            pfx = "READ" if fn in list_unread else "NEW "
            dist_ = datetime.datetime.now().timestamp() - os.path.getctime( os.path.join( dir_, fn ) )
            dist = string_helper.timedelta_to_string( dist_, approx = True )
            print( f"{pfx} {i: >5} {fn: <20} {dist} ago" )

        if arg_mark:
            # Mark all as read
            set_read_bn.update( os.path.basename( x ) for x in focus )
            io_helper.write_all_text( history_path, "\n".join( set_read_bn ) )
        elif arg_unmark:
            # Mark none as read
            list_unread.clear()
            io_helper.write_all_text( history_path, "\n".join( set_read_bn ) )

        return 0

    # Select the item to read
    if arg_id in ("first", "f"):
        index = 0
    elif arg_id in ("last", "l"):
        index = -1
    elif arg_id in ("review", "r"):
        first_unread = list_read[0]
        index = focus_.index( first_unread )
    elif arg_id:
        if arg_id.isdigit():
            index = int( arg_id )
        else:
            index = focus_.index( os.path.join( dir_, arg_id ) + extension )
    else:
        index = None

    if index is not None:
        try:
            fn = focus_[index]
        except IndexError:
            print( f"Nothing to read with this identifier ({index} must be in 0..{len( focus_ ) - 1})." )
            return 1

        text = io_helper.read_all_text( fn )

        import time
        ago = os.path.getctime( fn ) - time.time()
        ago_str = string_helper.timedelta_to_string( -ago, approx = True )
        is_read = "YES" if fn in list_unread else "NO"
        text = f"FILE NAME: {fn}\nTIME SINCE: {ago_str}\nIS READ: {is_read}\n{'-' * 80}\n{text}"

        if arg_pager:
            pydoc.pager( text )
        else:
            print( text )

        bn = os.path.basename( fn )
        set_read_bn.add( os.path.basename( bn ) )
        print( f"{bn} NOW MARKED AS READ." )

        if not arg_const:
            io_helper.write_all_text( history_path, "\n".join( set_read_bn ) )


if __name__ == "__main__":
    exit( _main() )
