"""
Minimal, non-extensible, LRU cache on-disk.

Thread and process safe.

Usage::
    from mhelper.disk_cache import disk_cache

    @disk_cache
    def my_function(x, y):
        return x + y

    my_function(x, y)


Internally, the cache is stored in files, with a hash based on:

    * The module name and the qualified function name
    * The function arguments
    * The function version (if provided)
    * The cache version (if provided)

:data disk_cache:

    A default `DiskCache` instance.
    To control the parameters, construct a new `DiskCache` instead, either via `DiskCache(...)` or
    `disk_cache.__class__(...)`.
"""
import sys
from typing import Optional, Callable, Tuple, Dict

from mhelper import io_helper, string_helper, file_helper, lock_helper
from mhelper.specific_locations import get_application_directory
import os
import functools

__all__ = "DiskCache", "disk_cache"

_sentinel = object()
_ArgsKwargs = Tuple[Tuple[object, ...], Dict[str, object], object]


class DiskCache:
    """
    DiskCache implementation.
    See module documentation for details.
    """
    __slots__ = ["__path",
                 "__max",
                 "__shared",
                 "__max_size",
                 "__version",
                 "__echo"]

    # region public

    def __init__( self,
                  name: Optional[str] = None,
                  max: int = 10,
                  max_size: int = 0,
                  version: object = None,
                  shared: bool = False,
                  echo: bool = False ):
        """
        :param name:    Name or path of the cache.
                        * `None` - ~/.rusilowicz/disk_cache/default is used.
                        * `str`, without '/' - ~/.rusilowicz/disk_cache/STRING is used.
                        * `str`, with '/' - STRING is used.
                        * `tuple` - ~/TUPLE is used.
                        Where `~` is the data directory defined by `specific_locations.get_application_directory`
                        and `/` is the system path separator.
        :param max:     Max files to keep in cache, per function. (LRU)
                        0 for unlimited count.
        :param max_size:Max files to keep in cache, in bytes, per function. (LRU)
                        0 for unlimited size.
        :param version: Denotes a version of the cache, thus ignoring cached values produced by a different version of
                        the cache.
        :param shared:  When set, all functions cache in the same path.
                        When unset, different functions cache in different subdirectories.

                        * Affects the meaning of `max`, which limits the directory size.
                        * Affects multi-threaded performance, which uses a per-directory lock.
        """
        if name is None:
            name = get_application_directory( "rusilowicz", "disk_cache", "default" )
        elif isinstance( name, str ):
            if os.path.sep in name:
                pass
            else:
                name = get_application_directory( "rusilowicz", "disk_cache", name )
        elif isinstance( name, tuple ):
            name = get_application_directory( *name )

        self.__path = name
        self.__max = max
        self.__shared = shared
        self.__max_size = max_size
        self.__version = version
        self.__echo = echo

    def __call__( self, fun: Optional[Callable] = None, *, version: object = None ):
        """
        Generates a decorator that wraps the function with the disk caching capability.

        The decorated function obtains the result from the cache, or caches and returns a new result.

        :param fun:     Internal. Allows `@decorator` instead of `@decorator()` syntax.
        :param version: Denotes the version of the function, cached values produced by a different version of the function will be ignored.
        :return:        Decorator.
        """

        def decorator( fun: Callable ):

            @functools.wraps( fun )
            def decorated( *args, **kwargs ):
                ak: _ArgsKwargs = args, kwargs, version
                r = self.__load_binary( fun, ak )

                if r is _sentinel:
                    r = fun( *args, **kwargs )
                    self.__save_binary( r, fun, ak )

                return r

            return decorated

        if fun is None:
            return decorator
        else:
            return decorator( fun )

    # endregion

    # region private

    def __print( self, message: str ) -> None:
        """
        Prints a message if echoing is enabled.
        :param message: The message. 
        """
        if not self.__echo:
            return

        print( message, file = sys.stderr )

    def __get_path( self, fun: Callable, ak: _ArgsKwargs ) -> str:
        """
        Gets the path of where to store the results for a function.
        :param fun: Function 
        :param ak:  Arguments 
        :return:    File path 
        """
        qn = self.__get_fun_name( fun )
        hash_src: str = self.__make_hash_source( (ak, qn, self.__version) )
        hash: str = string_helper.string_to_hash( hash_src )
        return os.path.join( self.__get_dir( fun ), hash ) + ".pkl"

    def __make_hash_source( self, data: object ) -> str:
        """
        Makes the hash input from the function arguments.
        :param data: Arguments 
        :return:     Hash 
        """
        r = repr( data )
        if string_helper.contains_pointers( r ):
            raise RuntimeError(
                    "disk_cache - Memory address in hash source. Please check for non-deterministic parameters." )
        return r

    def __get_dir( self, fun: Callable ) -> str:
        """
        Gets the data directory for the results of a function.
        :param fun: Function 
        :return:    Directory path 
        """
        qn = self.__get_fun_name( fun )

        if self.__shared:
            return self.__path
        else:
            r = os.path.join( self.__path, qn )
            os.makedirs( r, exist_ok = True )
            return r


    def __lock( self, fun: Callable ) -> lock_helper.FileLock:
        lfn: str = os.path.join( self.__get_dir( fun ), "disk_cache.lock" )
        return lock_helper.FileLock( lfn )

    def __purge( self, fun: Callable ) -> None:
        """
        Purges LRU results.
        :param fun: Function 
        """
        if not self.__max and not self.__max_size:
            return

            # Must be called from within lock
        directory = self.__get_dir( fun )
        files = file_helper.list_dir( directory )
        files_ = [(os.path.getmtime( x ), os.path.getsize( x ), x) for x in files]
        sz = sum( x[1] for x in files_ )
        files_ = sorted( files_, key = lambda x: x[0] )

        while ((self.__max and (len( files_ ) > self.__max))
               or (self.__max_size and (sz > self.__max_size))):
            file0t, file0s, file0n = files_.pop( 0 )
            sz -= file0s
            os.remove( file0n )

    def __get_fun_name( self, fun: Callable ):
        m = getattr( fun, "__module__" )
        q = getattr( fun, "__qualname__" )
        qn: str = f"{m}.{q}"
        return qn

    def __load_binary( self, fun: Callable, ak: _ArgsKwargs ) -> object:
        """
        Loads the data associated with a function.
        :param fun: Function 
        :param ak:  Arguments. 
        :return:    Results, or `_sentinel` if not available. 
        """
        with self.__lock( fun ):
            file_name: str = self.__get_path( fun, ak )

            if not os.path.isfile( file_name ):
                return _sentinel

            os.utime( file_name )
            r = io_helper.load_binary( file_name, default = _sentinel )

            if r is not _sentinel:
                self.__print( f"DiskCache - Existing ({os.path.getsize( file_name )}b): {file_name}" )

            return r

    def __save_binary( self, result: object, fun: Callable, ak: _ArgsKwargs ) -> None:
        """
        Saves the results for a function.
        :param result:  Result. 
        :param fun:     Function
        :param ak:      Arguments. 
        """
        with self.__lock( fun ):
            file_name: str = self.__get_path( fun, ak )
            self.__purge( fun )
            io_helper.save_binary( file_name, result )
            self.__print( f"DiskCache - New ({os.path.getsize( file_name )}b): {file_name}" )


    # endregion


disk_cache = DiskCache()
