"""
Common location helper
======================

Purpose
-------

Avoids having to put absolute paths to data files in scripts, allowing scripts
that rely on specific data to run, regardless of the machine.

Usage
-----
 
The user must have one or more "project roots" defined by the MJR_APPS_ALT
environment variable.

e.g. on computer#1::

    MJR_APPS_ALT = c:\\users\\martin\\projects;e:\\large_data_projects
    
And on computer#2::

    MJR_APPS_ALT = /home/martin/projects:/mnt/external/data
    
The the following command will locate a file, regardless of the computer::

    find_file( "my_project/my_file.txt" )
    
This would then return, on computer#1:

    c:\\users\\martin\\projects\\my_project\\my_file.txt
    
And on computer#2::

    /external/data/my_project/my_file.txt

For more details, see the documentation of the `find_all` function.


Configuration
-------------

If MJR_APPS_ALT is not specified, the PATH is used, but this is likely to either
be incorrect or provide many locations to search. A warning is issued to suggest
the user fix this behaviour.


Similar packages
----------------
    
See also the `specific_locations` module, which finds application-specific data.
"""
import os
import sys
from functools import lru_cache
from typing import Any, Callable, Iterable, Sequence, Union
import warnings

from mhelper import arg_parser, string_helper

__variants = "{}", "{}_partial"
__VAR = "MJR_APPS_ALT"
__PATH = "PATH"
__SEP = "/"
__FOR = "??"
__OR = "||"
__FILE_1 = "${VIRTUAL_ENV}/.mjr_apps_alt.txt"
__FILE_2 = "~/.mjr_apps_alt.txt"
__sentinel = object()
__ConstraintDelegate = Callable[[str], bool]
__DEFAULT_CONSTRAINT = os.path.exists


@lru_cache
def list_roots() -> Sequence[str]:
    """
    Root directories, governed by the `MJR_APPS_ALT` environment variable.
    
    See module documentation. 
    """
    env_var = os.environ.get( __VAR )

    if not env_var:
        warnings.warn( f"The system environment variable, `{__VAR}`, is missing or empty.\n"
                       f"This variable must be defined in order to denote the project root(s).\n"
                       f"I will try looking in the `{__PATH}` for now, but this may be incorrect.\n"
                       f"Please see the documentation at '{__file__}' for more details." )

        env_var = os.environ.get( __PATH )

    env_var = string_helper.replace_env( env_var )

    r = []

    for e in env_var.split( os.path.pathsep ):
        if not os.path.isdir( e ):
            continue

        r.append( e )

    return r


def list_projects():
    """
    Lists the projects in the root folder(s).
    """
    r = []

    for root_dir in list_roots():
        for fn in os.listdir( root_dir ):
            if fn.startswith( "." ):
                continue

            ffn = os.path.join( root_dir, fn )

            if not os.path.isdir( ffn ):
                continue

            if os.path.islink( ffn ):
                continue

            r.append( ffn )

    return r


def find_project( project: str ) -> str:
    """
    Finds a root project directory.
    
    :param project: Project name. 
    :return:        Absolute path. 
    """
    return find_file( project, constraint=os.path.isdir )


def find_file( term: Union[str, Iterable[str]],
               *args,
               default: Any = __sentinel,
               any: bool = False,
               constraint: __ConstraintDelegate = __DEFAULT_CONSTRAINT,
               **kwargs ) -> str:
    """
    Finds a file.
    See `find_all` for details.
    
    :param term:     See `find_all`.  
    :param args:     Passed to `find_all`.
    :param default:  Value to return should no match be found. 
    :param any:      When set, if there are multiple matches, we simply return the first.
                     When unset, if there are multiple matches we raise `FileNotFoundError`.
    :param kwargs:   Passed to `find_all`.
    :return:         Absolute path or `default`. 
    """
    allow_mk_dir = __FOR in term

    r = find_all( term, constraint=constraint )

    if not r:
        if default is __sentinel:
            raise FileNotFoundError( f"File not found.\n"
                                     f"\n"
                                     f"| A required file is missing:\n"
                                     f"|\n"
                                     f"|  * I cannot find any of the following:{__describe( term, constraint )}"
                                     f"  * In any directory defined by {__describe_alts()}"
                                     " *** Check the path is correct and that you have a copy of this data. ***" )

        return default
    elif len( r ) > 1 and not any:
        rs = "\n|".join( [f"      - '{x}'" for x in r] )
        raise FileNotFoundError( f"File not found.\n|A required file cannot be resolved:\n|"
                                 f"    * There are multiple matches for the following:{__describe( term, constraint )}"
                                 f"    * Across directories defined by {__describe_alts()}"
                                 f"    * These matches are:\n|\n|{rs}\n|\n|" )

    f = r[0]

    if allow_mk_dir:
        os.makedirs( os.path.dirname( f ), exist_ok=True )

    return f


def find_all( term: Union[str, Iterable[str]],
              *,
              constraint: __ConstraintDelegate = __DEFAULT_CONSTRAINT,
              ) -> Sequence[str]:
    """
    Find a file relative to one of the project roots (see `list_roots`).
    
    Always use "/" to delimit the path, regardless of platform.
    
    For example, to find an existing file:
    
        <== project/folder/file.txt
        ==> c:\my_projects\project\folder\file.txt
                    
    If you want to name a *new* file, to place in an existing directory, use
    "??" to specify a suffix (i.e. separate the part of the path that must exist
    from the part that may or may not exist)::
    
        <== project/folder??file.txt
        ==> c:\my_projects\project\folder\file.txt
        
    The leading (project) directory will also be searched against variants,
    such as "_partial"::
    
        <== project\folder\file.txt
        ==> c:\my_projects\project_partial\folder\file.txt
        
    Finally, we may use "||" to delimit multiple options.
    
        <== project/folder/file.txt||old_name/old_path/file.txt
        ==> c:\my_projects\project\folder\file.txt
            
    :param term:        Search term.
    :param constraint:  How to evaluate the part of the path that exists.
                        The default is `os.path.exists` but `os.path.isfile`
                        or `os.path.isdir` can be more explicit.
    """
    r = []

    if isinstance( term, str ):
        if __OR in term:
            terms = term.split( __OR )
        else:
            terms = None
    else:
        terms = term

    if terms is not None:
        results = []

        for term in terms:
            results.extend( find_all( term, constraint=constraint ) )

        return results

    #
    # Extract suffix, if present
    #
    if __FOR in term:
        term, suffix = term.split( __FOR )
        suffix = suffix.split( __SEP )
    else:
        suffix = ()

    terms = term.split( __SEP )

    for variant in __variants:
        term2 = os.path.join( variant.format( terms[0] ), *terms[1:] )
        __find_all( r, term2, constraint, suffix )

    return r


def __find_all( r, term, constraint, suffix ):
    for root in list_roots():
        file_name = os.path.join( root, term )

        if constraint( file_name ):
            file_name = os.path.join( file_name, *suffix )

            r.append( file_name )


def __describe_alts() -> str:
    xs = "\n|".join( [f"      - '{x}'" for x in list_roots()] )
    return f"the `{__VAR}` or `{__PATH}` environment variable:\n|\n|{xs}\n|\n|"


def __describe( term: Union[str, Iterable[str]],
                constraint: __ConstraintDelegate ) \
        -> str:
    if isinstance( term, str ):
        terms = term.split( __OR )
    else:
        terms = term

    xs = "\n|".join( [f"      - {__describe2( x )}" for x in terms] )

    if constraint is not __DEFAULT_CONSTRAINT:
        cn = "      (with constraint: " + getattr( constraint, "__name__", "?" ) + ")\n|\n|"
    else:
        cn=""

    return f"\n|\n|{xs}\n|\n|{cn}"


def __describe2( term: str ) -> str:
    if __FOR in term:
        prefix, suffix = term.split( __FOR, 1 )
        return f"{__describe2( prefix )} (in which to place {__describe2( suffix )})"

    x = os.path.sep.join( term.split( __SEP ) )
    return f"'{x}'"


def _main():
    arg_parser.reflect( __main )


def __main( file_name: str ):
    matches = find_all( file_name )

    for ffn in matches:
        print( ffn )

    if not matches:
        print( f"No matches.", file=sys.stderr )


def is_executable( file_name: str ) -> bool:
    if not os.path.isfile( file_name ):
        return False

    return os.access( file_name, os.X_OK )


if __name__ == "__main__":
    _main()
