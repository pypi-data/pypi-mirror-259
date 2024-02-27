"""
Deprecated - too specific use case.

Use lru_cache
"""
from typing import Tuple

from mhelper import string_helper


MISS = object()


class Parameters:
    def __init__( self, *args, **kwargs ):
        self.args = args
        self.kwargs = kwargs
    
    
    def to_sequence( self ) -> Tuple[Tuple[str, object], ...]:
        r = (
            *((str( i ), v) for i, v in enumerate( self.args )),
            *self.kwargs.items()
            )
        return tuple( sorted( r, key = lambda x: x[0] ) )


class Key:
    def __init__( self, parameters: Parameters, key: object ):
        self.parameters = parameters
        self.key = key


class ICache:
    
    def read( self ):
        raise NotImplementedError( "abstract" )
    
    
    def write( self, value ):
        raise NotImplementedError( "abstract" )


class ICacheMap:
    def map( self, params: Parameters ) -> ICache:
        raise NotImplementedError( "abstract" )
    
    
    def cached( self, fn = None ):
        if fn:
            return _CachingFunction( self, fn )
        else:
            return self.cached


class KeyedCache( ICache ):
    def __init__( self, cache_map, key: object ):
        self.cache_map = cache_map
        self.key = key
    
    
    def read( self ) -> object:
        return self.cache_map.read( self.key )
    
    
    def write( self, value: object ) -> None:
        return self.cache_map.write( self.key, value )


class KeyedCacheMap( ICacheMap ):
    def map( self, params: Parameters ) -> ICache:
        key = Key( params, self.to_key( params ) )
        return KeyedCache( self, key )
    
    
    def to_key( self, params: Parameters ) -> object:
        r = params.to_sequence()
        txt = "\n".join( f"{k}\t{v!r}" for k, v in r )
        return string_helper.string_to_hash( txt )
    
    
    def read( self, key: Key ) -> object:
        pass
    
    
    def write( self, key: Key, value: object ) -> None:
        pass


class _CachingFunction:
    __slots__ = "cache_map", "function"
    
    
    def __init__( self, cache_map, function ):
        self.cache_map = cache_map
        self.function = function
    
    
    def __call__( self, *args, **kwargs ):
        key = Parameters( self.function, *args, **kwargs )
        
        cache = self.cache_map.map( key )
        
        cached = cache.read()
        
        if cache is not MISS:
            return cache
        
        r = self.function( *args, **kwargs )
        
        cached.write( r )
        
        return r
