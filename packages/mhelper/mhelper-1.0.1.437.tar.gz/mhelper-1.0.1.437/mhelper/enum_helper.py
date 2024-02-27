from enum import Enum, EnumMeta
from typing import Type, Union, Any, TypeVar


def _set( d, k, v ):
    c = d.get( k )
    
    if c is v:
        return
    
    if c is None:
        d[k] = v
        return
    
    raise ValueError( f"Duplicate key: {k} = {c} != {v}" )


class VagueEnumMeta( EnumMeta ):
    def __init__( cls, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        
        m = { }
        
        for key, value in cls.__dict__.items():
            if not isinstance( value, cls ):
                continue
            
            _set( m, key.lower(), value )
            _set( m, value.name.lower(), value )
            
            v = value.value
            
            if isinstance( v, str ):
                v = v.lower()
            
            _set( m, v, value )
            _set( m, v, value )
        
        cls._vem_map = m
    
    
    def __contains__( cls, item ):
        return cls._get( item ) is not None
    
    
    def _get( cls, item ):
        if isinstance( item, str ):
            item = item.lower()
        
        return cls._vem_map.get( item, None )


class VagueEnum( Enum, metaclass = VagueEnumMeta ):
    """
    An Enum derivative that permits comparison to the name and value.
    
    This allows the caller to compare against the enum, for instance by naming
    the member, without the class itself having to be imported by the caller.
    
    If the value itself is string typed, then string comparisons will be made
    against a the *value* and not the name.
    
    String comparisons to the name or value are case insensitive.
    
    Note that 1 == True and 0 == False, which permits comparison to `bool`.
    """
    
    
    def __eq__( self, other ):
        if type( other ) is type( self ):
            return super().__eq__( other )
        
        return super().__eq__( type( self )._get( other ) )


# VagueEnum: Type[object]

TEnum = TypeVar( "TEnum", bound = Enum )


def map_enum( t: Type[TEnum], v: Union[str, int, TEnum] ) -> TEnum:
    if type( v ) is t:
        return v
    
    if isinstance( v, str ):
        from mhelper import string_helper
        return string_helper.string_to_enum( t, v )
    
    return t( v )


def get_enum_title( x: Enum ):
    """
    Obtains the "title" of an `Enum` member.
    
    * The first line of its cvar documentation
    * The enum name
    """
    
    from mhelper.documentation_helper import Documentation
    v = Documentation( type( x ).__doc__ ).get_element( "cvar", x.name )
    
    if v:
        if "\n" in v:
            v = v.split( "\n", 1 )[0]
        
        v = v.strip()
        v = v.rstrip( "." )
        
        return v
    else:
        return x.name


def rebind( e: Enum ):
    return e.__class__[e.name]


def __test():
    class MyVagueEnum( VagueEnum ):
        ALPHA = 1
        BETA = 2
        GAMMA = 3
    
    
    assert MyVagueEnum.ALPHA == "alpha"
    assert MyVagueEnum.ALPHA != "beta"
    assert "Beta" == MyVagueEnum.BETA
    assert "Alpha" != MyVagueEnum.BETA
    assert MyVagueEnum.GAMMA == "GAMMA"
    assert MyVagueEnum.GAMMA != "ALPHA"
    
    assert MyVagueEnum.ALPHA == 1
    assert MyVagueEnum.ALPHA != 2
    assert 2 == MyVagueEnum.BETA
    assert 1 != MyVagueEnum.BETA
    assert MyVagueEnum.GAMMA == 3
    assert MyVagueEnum.GAMMA != 1
    
    assert MyVagueEnum.ALPHA == MyVagueEnum.ALPHA
    assert MyVagueEnum.ALPHA != MyVagueEnum.BETA
    assert MyVagueEnum.BETA == MyVagueEnum.BETA
    assert MyVagueEnum.BETA != MyVagueEnum.ALPHA
    assert MyVagueEnum.BETA != MyVagueEnum.GAMMA
    
    assert map_enum( MyVagueEnum, "ALPHA" ) == MyVagueEnum.ALPHA
    assert map_enum( MyVagueEnum, MyVagueEnum.ALPHA ) == MyVagueEnum.ALPHA
    assert map_enum( MyVagueEnum, 1 ) == MyVagueEnum.ALPHA
    assert map_enum( MyVagueEnum, "BETA" ) != MyVagueEnum.ALPHA
    assert map_enum( MyVagueEnum, MyVagueEnum.BETA ) != MyVagueEnum.ALPHA
    assert map_enum( MyVagueEnum, 2 ) != MyVagueEnum.ALPHA
    
    print( f"{__file__}: all tests passed ok" )


if __name__ == "__main__":
    __test()
