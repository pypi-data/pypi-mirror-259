"""
Obtains a location in which to store application data.

By default we create such data-folders:

* in the folder defined by the ``MJR_APPS_DATA`` environment variable
* inside the virtual environment
* within the user's home directory

The first valid option is selected for new data-folders, but if the data-folder
already exists in any of these directories, this is always used.
 
.. hint::

    Set ``MJR_APPS_DATA`` to share data between multiple applications, or
    multiple installs of the same application).

See `get_application_data_root` for full path resolution details.
"""
import os as _os
import sys as _sys
from functools import lru_cache as _lru_cache

__ENV_VAR_NAME = "MJR_APPS_DATA"


@_lru_cache
def get_application_data_root() -> str:
    """
    Gets the "home" folder in which we place the application data folders.
                 
    :returns:    Absolute path
    """
    cust_dir = _os.getenv( __ENV_VAR_NAME )

    if cust_dir:
        if not _os.path.isdir( cust_dir ):
            raise ValueError( f"The environment variable `{__ENV_VAR_NAME}` is defined but the path it points to ({cust_dir}) does not exist." )

        return cust_dir

    if _sys.prefix != _sys.base_prefix:
        venv_dir = _sys.prefix

        if not _os.path.isdir( venv_dir ):
            raise ValueError( f"The environment variable `VIRTUAL_ENV` is defined but the path it points to ({venv_dir}) does not exist." )

        return _os.path.join( venv_dir, "mjr_app_data" )

    default_dir = _os.path.expanduser( "~" )

    if not _os.path.isdir( default_dir ):
        raise ValueError( f"The home directory `~` ({default_dir}) does not exist." )

    return default_dir


def get_application_directory( *args, mkdir = True ) -> str:
    """
    Gets a directory for an application's settings.
    See module comments for how this is resolved.
        
    :param args:    Elements of the path, for instance::
                    
                        application
                        developer/application                    
                        developer/application/caches
                        
                    Elements may be specified as a slash-delimited path
                    (regardless of platform) *or* a series of arguments, e.g.
                    
                        get_application_directory("developer/application")
                        get_application_directory("developer", "application") 
                         
    :param mkdir:   When set, the directory is created if it doesn't already
                    exist. 
                    
    :return:    Absolute path to the directory. 
    """
    args = __parse_path( args )

    root = get_application_data_root()

    path = _os.path.join( root, *args )

    if mkdir:
        _os.makedirs( path, exist_ok = True )

    return path


def get_application_file_name( *args, mkdir = True ) -> str:
    """
    Calls `get_application_directory` and appends the file-name.
    See `get_application_directory` for details.
    """
    args = __parse_path( args )
    directory = get_application_directory( *args[:-1], mkdir = mkdir )
    return _os.path.join( directory, args[-1] )


def __parse_path( args ):
    r = []

    for arg in args:
        if isinstance( arg, str ):
            r.extend( arg.split( "/" ) )
        else:
            assert all( isinstance( x, str ) for x in arg )
            r.extend( arg )

    if not r[0].startswith( "." ):
        r[0] = f".{r[0]}"

    return r
