"""
Helper containing the `CachedRequest`, for making HTTP requests and and 
maintaining a common cache of data.

REQUIRES: filelock, requests 
"""
# !EXPORT_TO_README
import os
import warnings
from time import sleep

from mhelper import file_helper, string_helper, log_helper, lock_helper, io_helper


request_log = log_helper.MLog( "mhelper.web_helper.cached_request" )
request_log_ex = log_helper.MLog( "mhelper.web_helper.cached_request_ex" )

NO_FILE = ('', '')


class CachedRequest:
    """
    Class for making HTTP requests.
    
    * Responses are cached to disk.
    * Requests are file-locked, to ensure multiple instances of the application do not conflict.
    
    
    """
    __info_messages = set()
    NO_FILE = NO_FILE


    def __init__( self,
                  url,
                  *,
                  dir = None,
                  headers = None,
                  throttle = 0,
                  data = None,
                  cache = True,
                  files = None,
                  fake = True,
                  cache_key = None,
                  retries = 3,
                  retry_throttle = 3,
                  timeout = 20,
                  check_status_code = False,
                  ):
        """
        Makes an HTTP request, caching the result.
        Note that only the URL and data are used as the cache keys by default.
        Other fields may be present but are disregarded from the cache.
        
        Requires the `requests` library.
        
        :param url:          Target URL. Including any GET query.
        :param dir:          Directory to store cached files in.
                             If this is a tuple `get_application_directory` will be used.
                             The default is "rusilowicz", "web_helper", "cache" 
        :param headers:      Request headers. 
        :param throttle:     Throttle (delay) requests. 
        :param data:         POST data, if any. 
        :param cache:        Whether to restore an existing cached.
                             When `false` the cache will be regenerated. 
        :param files:        POST data files, if any. 
        :param fake:         Fake user-agent, origin and referer, if not in `headers`. Required by some forms.
        :param cache_key:    Key to use for the cache. Uses the `url` and `data` if not specified.
                             This is only useful where the URL/data is fixed but the result is dependent on an earlier operation.
        :return:             Page data. 
        """

        self.url = url
        self.headers = headers
        self.throttle = throttle
        self.data = data
        self.cache = cache
        self.files = files
        self.cache_key = cache_key
        self.retries = retries
        self.retry_throttle = retry_throttle
        self.timeout = timeout
        self.check_status_code = check_status_code

        if self.cache_key is None:
            cache_key = self.url + repr( self.data )

        if fake:
            if self.headers is None:
                self.headers = { }

            referer = self.url.split( "?", 1 )[0]
            origin = "/".join( self.url.split( "/", 3 )[:3] )

            self.headers.setdefault( 'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' )
            self.headers.setdefault( "Origin", origin )
            self.headers.setdefault( "Referer", referer )
            self.headers.setdefault( "Accept-Language", "en-GB,en;q=0.5" )

        self.cache_directory = self.__resolve_cache_directory( dir )

        cache_key = str( cache_key )
        request_log_ex( "The key is: {}", cache_key )
        hash = string_helper.string_to_hash( cache_key )
        file_name = os.path.join( self.cache_directory, hash + ".html" )
        self.cache_file_name = file_name
        self.title = self.url.split( "/", 3 )[2]


    @staticmethod
    def get_default_cache_folder():
        return file_helper.get_application_directory( "rusilowicz", "web_helper", "cache" )


    def __repr__( self ):
        return f"{self.__class__.__name__}( url = {self.url!r}, cache_file = {self.cache_file_name!r} )"


    def __str__( self ):
        return f"{self.url!r} (cached: {self.cache_file_name!r})"


    def get_cached( self ):
        if not os.path.isfile( self.cache_file_name ):
            request_log_ex( "Not in cache: {}", self.cache_file_name )
            return None

        result = file_helper.read_all_text( self.cache_file_name )
        request_log_ex( "Is in cache: {}", self.cache_file_name )
        return result


    def get_lock( self ):
        return lock_helper.FileLock( self.cache_file_name + ".rcz.lock" )

    def download( self ):
        self.get()
        return self.cache_file_name

    def get( self ):
        try:
            # noinspection PyPackageRequirements
            import requests
        except ImportError as ex:
            raise ImportError( "This feature requires the requests library, which is not currently installed." ) from ex

        if self.cache_directory not in self.__info_messages:
            request_log( "The web cache at {} is {}", self.cache_directory, string_helper.format_size( CachedRequest.get_total_cache_size( self ) ) )
            self.__info_messages.add( self.cache_directory )

        r = self.get_cached() if self.cache else None

        if r is not None:
            request_log( "Already cached. ({})", self.title )
            return r

        with self.get_lock():
            r = self.get_cached() if self.cache else None

            if r is not None:
                request_log( "Already cached by another process. ({})", self.title )
                return r

            request_log( "Contacting server... ({})", self.title )

            if self.throttle:
                sleep( self.throttle )

            if self.data is None and self.files is None:
                method = "GET"
            else:
                method = "POST"

            request = None

            while True:
                try:
                    request = requests.request( method = method,
                                                url = self.url,
                                                data = self.data,
                                                headers = self.headers,
                                                files = self.files,
                                                timeout = self.timeout )

                    if self.check_status_code and request.status_code != 200:
                        raise ConnectionError( f"Bad status code: {request.status_code}" )
                except Exception as ex:
                    if self.retries:
                        request_log( "No response, retrying in {} seconds... ({})", self.retry_throttle, self.title )
                        sleep( self.retry_throttle )
                        self.retries -= 1
                        continue

                    message = [f"Request failed:",
                               f"",
                               f"import requests",
                               f"requests.request(",
                               f"    method = {method!r}",
                               f"    url = {self.url!r}",
                               f"    data = {self.data!r}",
                               f"    headers = {self.headers!r}",
                               f"    files = {self.files!r} )",
                               f"",
                               f"Due to an error",
                               f"{ex.__class__.__qualname__}: {ex}"]

                    raise ConnectionError( "\n".join( message ) )
                else:
                    break

            request_log( "Contacted OK. Code {}. ({})", request.status_code, self.title )

            result = request.text
            io_helper.write_all_text( self.cache_file_name, result )
            request_log_ex( "Saved to cache: {}", self.cache_file_name )

            return result


    def uncache( self ):
        """
        Removes the cached data from disk.
        
        Useful if the response turned out to be bad due to some non-permanent error. 
        """
        with self.get_lock():
            if os.path.isfile( self.cache_file_name ):
                request_log( "Uncaching ({})", self.title )
                os.remove( self.cache_file_name )


    @staticmethod
    def __resolve_cache_directory( dir ):
        if not dir:
            return CachedRequest.get_default_cache_folder()

        if isinstance( dir, str ):
            os.makedirs( dir, exist_ok = True )
            return dir
        else:
            return file_helper.get_application_directory( *dir )


    @staticmethod
    def get_total_cache_size( x = None ):
        """
        Indicates the total size of all cached data.
        """
        if isinstance( x, CachedRequest ):
            x = x.cache_directory
        else:
            x = CachedRequest.__resolve_cache_directory( x )

        return file_helper.get_directory_tree_size( x )


def cached_request( *args, **kwargs ):
    warnings.warn( "Deprecated - use CachedRequest", DeprecationWarning )
    return CachedRequest( *args, **kwargs ).get()


def get_cache_file_name( *args, **kwargs ):
    warnings.warn( "Deprecated - use CachedRequest", DeprecationWarning )
    return CachedRequest( *args, **kwargs ).cache_file_name


def get_cache_size( *args, **kwargs ) -> int:
    warnings.warn( "Deprecated - use CachedRequest", DeprecationWarning )
    return CachedRequest.get_total_cache_size( *args, **kwargs )


def uncache( *args, **kwargs ):
    warnings.warn( "Deprecated - use CachedRequest", DeprecationWarning )
    return CachedRequest( *args, **kwargs ).uncache()
