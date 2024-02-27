"""
Defines various special but commonly used classes:

* a Sentinel class
* a `NOT_PROVIDED` sentinel
* ArgsKwargs
* a Booly class (because `bool` can't be subclassed)
* a namespace that is also a dict (NamespaceDict) 
"""
# !EXPORT_TO_README
from enum import Enum, EnumMeta, Flag
from typing import TypeVar, Optional, Iterable, Type


T = TypeVar( "T" )
"""
General purpose typevar.
"""

TTristate = Optional[bool]
"""
An optional boolean
"""


def identity( x: T ) -> T:
    """
    General purpose pass through.
    """
    return x


def ignore( *_, **__ ):
    """
    No-pass-through, used to ignore parameters, etc.
    """
    pass


class Sentinel:
    """
    Type used for sentinel objects (things that don't do anything but whose presence indicates something).
    The Sentinel also has a `str` method equal to its name, so is appropriate for user feedback. 
    """
    
    
    def __init__( self, name: str ):
        """
        :param name:    Name, for debugging or display. 
        """
        self.__name = name
    
    
    def __str__( self ) -> str:
        return self.__name
    
    
    def __repr__( self ):
        return "Sentinel({})".format( repr( self.__name ) )


class NotProvidedType( Sentinel ):
    """
    The type of NOT_PROVIDED
    """
    pass


NOT_PROVIDED : NotProvidedType = NotProvidedType( "(Not provided)" )
"""
NOT_PROVIDED is used to distinguish between a value of `None` and a value that that isn't even provided.
"""


# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ▒ ENUMS ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


class MEnum( Enum ):
    """
    An enum class that presents a less verbose string function
    """
    
    
    def __str__( self ):
        return self.name


class MFlagMeta( EnumMeta ):
    """
    Type of `MFlag`.
    """
    
    
    def __getitem__( cls, item ):
        return cls.from_string( item )
    
    
    def from_string( cls, text, delimiter = "|" ):
        elements = text.split( delimiter )
        r = super().__getitem__( elements[0] )
        for it in elements[1:]:
            r |= super().__getitem__( it )
        return r


class MFlag( Flag, metaclass = MFlagMeta ):
    """
    A flag class that presents a less verbose string function
    """
    
    
    def __str__( self ):
        return self.to_string()
    
    
    def to_string( self, delimiter = "|" ):
        text = super().__str__().replace( "{}.".format( type( self ).__name__ ), "" )
        its = text.split( "|" )
        return delimiter.join( reversed( its ) )


_default_filename_path = None


class ArgsKwargs:
    EMPTY: "ArgsKwargs" = None
    
    
    def __init__( self, *args, **kwargs ) -> None:
        self.args = args
        self.kwargs = kwargs
    
    
    def __bool__( self ):
        return bool( self.args ) or bool( self.kwargs )
    
    
    def __getitem__( self, item ):
        r = self.get( item[0], item[1] )
        
        if r is NOT_PROVIDED:
            raise KeyError( item )
        
        return r
    
    
    def get( self, index, name, default = NOT_PROVIDED ):
        if 0 <= index < len( self.args ):
            return self.args[index]
        
        if name:
            return self.kwargs.get( name, default )
        
        return default
    
    
    def __repr__( self ):
        r = []
        
        for x in self.args:
            r.append( "{}".format( x ) )
        
        for k, x in self.kwargs.items():
            r.append( "{} = {}".format( k, x ) )
        
        return ", ".join( r )


class Booly:
    """
    Wraps a value (e.g. an annotation), while providing a `__bool__` status.
    
    Example::
    
        return Booly.TRUE("Connected") if x else Booly.FALSE("Could not connect")
    
    :cvar TRUE: True class
    :cvar FALSE: True class
    :cvar _boolean_value: Actual boolean value
    """
    __slots__ = "value",
    _boolean_value = None
    TRUE: Type["__Truthy"] = None
    FALSE: Type["__Falsy"] = None
    
    
    def __init__( self, value: object ):
        self.value = value
    
    
    def __repr__( self ):
        return "Boolean({}, {})".format( repr( self._boolean_value ), repr( self.value ) )
    
    
    def __bool__( self ) -> bool:
        return self._boolean_value


class __Truthy( Booly ):
    __slots__ = ()
    _boolean_value = True


class __Falsy( Booly ):
    __slots__ = ()
    _boolean_value = False


Booly.TRUE = __Truthy
Booly.FALSE = __Falsy


class NamespaceDict( dict ):
    """
    A ganeral purpose namespace object.
    i.e. a `dict` that can be accessed through its attributes (get only).
    """
    
    
    def __getattr__( self, item ):
        return self[item]
    
    
    def __dir__( self ) -> Iterable[str]:
        return tuple( frozenset( super().__dir__() ).union( frozenset( self.keys() ) ) )


ArgsKwargs.EMPTY = ArgsKwargs()
