"""
Deprecated - no longer applicable from Python 3.7 with the new release of the `typing` library.
"""
# !EXPORT_TO_README
from typing import Any, Callable, Optional, Type, TypeVar, Union, cast, Sequence, Generic, Tuple, Dict, get_args

# Decorator function, returns a function that takes and returns a function
import typing

from mhelper import string_helper, exception_helper


DECORATOR_FUNCTION = Callable[..., Callable[[Callable], Callable]]
# Decorator - takes a function, returns a function
DECORATOR = Callable[[Callable], Callable]
DECORATED = Optional[object]

T = TypeVar( "T" )


class ByRef( Generic[T] ):
    """
    Pass value by reference.
    """
    __slots__ = ["value"]
    
    
    def __init__( self, value: T = None ):
        self.value: T = value


def extend( type_ ):
    """
    Adds an extension method.
    :param type_:   Type to extend 
    :return: 
    """
    
    
    def ___fn( fn ):
        setattr( type_, fn.__name__, fn )
        return fn
    
    
    return ___fn


class GenericPopulator:
    def __init_subclass__( cls, **kwargs ):
        type_args_list = []
        
        for base in cls.mro():
            if not hasattr( base, "__orig_bases__" ):
                continue
            
            for orig_base in getattr( base, "__orig_bases__" ):
                type_args = typing.get_args( orig_base )
                
                if type_args:
                    type_args_list.append( type_args )
                    
                    if len( type_args_list ) > 2:
                        # derived from already generic (multiple repeats)
                        return
        
        if len( type_args_list ) < 2:
            # Not derived enough (only TypeVars) or nothing
            return
        
        for generic_type, generic_typevar in zip( *type_args_list ):
            field_name = string_helper.undo_camel_case( generic_typevar.__name__, sep = "_" ).upper()
            
            if getattr( cls, field_name, None ) is not generic_typevar:
                raise RuntimeError( f"Expected placeholder for {cls.__name__}.{field_name}." )
            
            setattr( cls, field_name, generic_type )


class TypedList( Generic[T] ):
    __slots__ = "__list",
    
    
    def get_list_type( self ):
        return self.__parameters__[0]
    
    
    def __init__( self, *args, **kwargs ):
        self.__list = list( *args, **kwargs )
    
    
    def __getitem__( self, item ):
        return self.__list[item]
    
    
    def __setitem__( self, key, value ):
        self.__check_instance( value )
        self.__list[key] = value
    
    
    def append( self, value ):
        self.__check_instance( value )
        self.__list.append( value )
    
    
    def __check_instance( self, value ):
        if not isinstance( value, self.__parameters__[0] ):
            raise TypeError( "Value «{}» of incorrect type «{}» added to list of «{}».".format( value, type( value ), self.get_list_type() ) )


class NestedSequence( Sequence[T] ):
    __slots__ = "__collection",
    
    
    def __init__( self, items: Sequence[T] ):
        self.__collection = items
    
    
    def __iter__( self ):
        return iter( self.__collection )
    
    
    def __len__( self ):
        return len( self.__collection )
    
    
    def __getitem__( self, item ):
        return self.__collection.__getitem__( item )
    
    
    def __bool__( self ):
        return bool( self.__collection )
    
    
    def __repr__( self ):
        return f"{self.__class__.__name__}( {self.__collection!r} )"
    
    
    def __str__( self ):
        return self.__collection.__str__()


class AutoReprMixin:
    def __repr__( self ):
        import mhelper.debug_helper
        return mhelper.debug_helper.dump_repr( self )


class _BoundTypeVar:
    """
    A `TypeVar` and the `Type` that it is used in.
    
    Comparable to itself and a tuple of `Type` and `TypeVar`.
    
    .. note::
    
        This class is internal - it may be substituted for a
        `Tuple[Type, TypeVar]` when making queries.
    """
    __slots__ = "klass", "type_var"
    
    
    def __init__( self, klass, type_var ):
        self.klass = klass
        self.type_var = type_var
    
    
    def __repr__( self ):
        return f"_BoundTypeVar({self.klass.__qualname__}, {self.type_var.__name__})"
    
    
    def __eq__( self, other ):
        if isinstance( other, tuple ) and len( other ) == 2:
            return other[0] is self.klass and other[1] is self.type_var
        
        if not type( other ) is _BoundTypeVar:
            return False
        
        return other.klass is self.klass and other.type_var is self.type_var
    
    
    def __hash__( self ):
        return hash( (self.klass, self.type_var) )


class TypeVarMap:
    """
    Maps a class to its type arguments.
    
    .. important::
    
        Only works with the first base class of each derived class at present.
    
    :ivar absolute_map:     Maps each `_BoundTypeVar`...
                            ...to its assigned _BoundTypeVar or Type
    :ivar reversed_map:     Maps each `_BoundTypeVar`... 
                            ...to the _BoundTypeVar it is assigned to. 
    :ivar normalised_map:   Maps each `_BoundTypeVar`...
                            ...to the `Type` it is ultimately assigned to.
    :ivar unbound_map:      Maps each TypeVar...
                            ...to the Type is it ultimately assigned to, or
                            `None` if the `TypeVar` is used in multiple bases.
    """
    absolute_map: typing.Dict[_BoundTypeVar, Union[_BoundTypeVar, Type]]
    reversed_map: Dict[_BoundTypeVar, _BoundTypeVar]
    normalised_map: Dict[_BoundTypeVar, Type]
    
    
    def __init__( self, klass ):
        if not isinstance( klass, type ):
            klass = type( klass )
        
        last = []
        r = { }
        
        for base in reversed( klass.mro() ):
            y = getattr( base, "__orig_bases__", None )
            
            if not y:
                continue
            
            pending = []
            y = typing.get_args( y[0] )
            
            for arg_n in y:
                value = _BoundTypeVar( base, arg_n )
                
                key = last.pop( 0 ) if last else None
                
                if isinstance( arg_n, TypeVar ):
                    pending.append( value )
                    
                    if key is not None:
                        r[key] = value
                elif key is not None:
                    r[key] = arg_n
            
            last = pending
        
        self.absolute_map = r
        
        rev_map = { }
        
        for key, value in self.absolute_map.items():
            if isinstance( value, _BoundTypeVar ):
                rev_map[value] = key
        
        self.reversed_map = rev_map
        
        norm_map = { }
        norm_ub_map = { }
        
        for key, value in self.absolute_map.items():
            while key in rev_map:
                key = rev_map[key]
            
            norm_map[key] = value
            
            key = key.type_var
            
            if key in norm_ub_map:
                norm_ub_map[key] = None
            else:
                norm_ub_map[key] = value
        
        self.normalised_map = norm_map
        self.unbound_map = norm_ub_map
    
    
    def __getitem__( self, item: Union[Type, Tuple[Type, TypeVar], _BoundTypeVar] ) -> Type:
        """
        :param item: Either a `TypeVar` or a tuple of `Type` and `TypeVar`.  
        :return:     Value in the `normalised_map` to which `item` is assigned.
        :exception MultipleError: Only `TypeVar` was specified and this `TypeVar` has been reused
                                  in multiple bases. 
        """
        if not isinstance( item, TypeVar ):
            return self.normalised_map[item]
        else:
            r = self.unbound_map[item]
            if r is None:
                raise exception_helper.MultipleError( f"The TypeVar {item!r} is bound in multiple classes. Please specify the class when calling f{TypeVarMap.__getitem__.__name__}" )
            return r
    
    
    def __repr__( self ):
        return f"{type( self ).__name__}({self.normalised_map!r})"


