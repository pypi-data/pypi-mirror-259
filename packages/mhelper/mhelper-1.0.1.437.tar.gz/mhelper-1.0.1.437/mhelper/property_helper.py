"""
Various property related helpers:

* Indexable properties
* Frozen classes
* Class properties 
"""
# !EXPORT_TO_README
import functools
from typing import Type, TypeVar, Union, Callable, Optional
from mhelper import exception_helper


T = TypeVar( "T" )


def itemproperty( f ):
    """
    Like the `@property` decorator, but creates an indexable property.
    
    Note that the _setter_ is called `itemsetter` and not `setter`.
    (This is to avoid PyLint or IDEs being confused as they make certain assumptions about `.setter` decorators.)
    
    ```
    class MyClass:
        @itemproperty
        def eggs( item ):
            return self._eggs[item]
            
        @eggs.itemsetter
        def eggs( item, value ):
           self._eggs[item] = value 
    
    m = MyClass()
    m.eggs["spam"] = "beans"
    print( m.eggs["spam"] )
    ``` 
    """
    return _ItemPropertyClass( f )


class _ItemPropertyClass:
    def __init__( self, getter ):
        self._getter = getter
        self._setter = None
    
    
    def __get__( self, instance, owner ):
        return _BoundItemPropertyClass( instance, self )
    
    
    def itemsetter( self, setter ):
        self._setter = setter
        return self


class _BoundItemPropertyClass:
    def __init__( self, self2, class_: _ItemPropertyClass ):
        self.__self2 = self2
        self.__class = class_
    
    
    def __getitem__( self, item ):
        return self.__class._getter( self.__self2, item )
    
    
    def __setitem__( self, key, value ):
        return self.__class._setter( self.__self2, key, value )


class FrozenAttributes:
    """
    Prevents adding attributes to the class after __init__ has been called.
    """
    __KEY = "_FrozenAttributes__lock"
    
    
    def __init__( self ):
        setattr( self, FrozenAttributes.__KEY, None )
    
    
    def __setattr__( self, key: str, value: object ) -> None:
        """
        Prohibits new attributes being set on this class.
        This guards against functionless legacy setup.  
        """
        if hasattr( self, FrozenAttributes.__KEY ) and not hasattr( self, key ):
            raise TypeError( "Unrecognised attribute on «{}»".format( type( self ) ) )
        
        object.__setattr__( self, key, value )


class Immutable:
    """
    Prevents changing attributes or their values on the object after __init__ has been called.
    """
    __slots__ = "_FrozenValues__lock",
    __KEY = "_FrozenValues__lock"
    
    
    def __init__( self ):
        object.__setattr__( self, FrozenValues.__KEY, None )
    
    
    def __setattr__( self, key: str, value: object ) -> None:
        """
        Prohibits new attributes being set on this class.
        This guards against functionless legacy setup.  
        """
        if hasattr( self, FrozenValues.__KEY ):
            raise TypeError( "Cannot change attributes on a `{}( Immutable )` object after it has been initialised.".format( type( self ).__qualname__ ) )
        
        object.__setattr__( self, key, value )


FrozenValues = Immutable


def null_coalesce( *args: T ) -> T:
    for arg in args:
        if arg is not None:
            return arg
    
    return None


def null_coalesce_attrs( object_, *fields, type: Type[T] = object ) -> T:
    for field in fields:
        if object_ is None:
            return None
        
        object_ = getattr( object_, field )
    
    return object_


class read_only_class_property( object ):
    """
    Defines a read-only-class-property
    
    Usage:
    
        @read_only_class_property
        def fn( cls ):
            pass
            
    OR:

        @read_only_class_property
        @classmethod
        def fn( cls ):
            pass
        
    OR:

        @classmethod    
        def _fn( cls )
            pass
            
        fn = read_only_class_property( _fn )
        
    Method 1 may issue a linter warning because the method isn't seen as a class
    method and so `cls` should be named `self`. Method 2 may issue a warning
    because "This decorator will not receive a callable it may expect". Method
    3 issues no warning but is more verbose. Renaming `cls` to `self` in method
    1 also works, but can be confusing.
    """
    __slots__ = ["fn"]
    
    
    def __init__( self, fn: Union[Callable, classmethod] ):
        """
        :param fn:  The function to decorate.
                    If this is alreafdy decorated with `classmethod`, it is 
                    unwrapped.  
        """
        if isinstance( fn, classmethod ):
            fn = fn.__func__
        
        self.fn = fn
    
    
    def __get__( self, obj, owner ):
        return self.fn( owner )


__cached_value_attr = "cached_value"


def cached( fn ):
    """
    A decorator that caches the function's value the first time it is called.
    
    To uncache the value, use `uncache`.
    """
    
    
    @functools.wraps( fn )
    def _rfn():
        try:
            return getattr( fn, __cached_value_attr )
        except AttributeError:
            r = fn()
            setattr( fn, __cached_value_attr, r )
            return r
    
    
    return _rfn


def uncache( fn ):
    """
    Uncaches the cached value on a function cached by `cached`.
    """
    delattr( fn, __cached_value_attr )


class ClassCallOverridableMeta( type ):
    """
    Exposes an `_on_class_call` method that allows the class's __call__ to be
    overridden using the actual type.
    """
    
    
    def __call__( cls, *args, **kwargs ):
        return cls._on_class_call( *args, **kwargs )
    
    
    def _on_class_call( cls, *args, **kwargs ):
        return type.__call__( cls, *args, **kwargs )


class ClassCallOverridable( metaclass = ClassCallOverridableMeta ):
    """
    See `ClassCallOverridableMeta`.
    """
    
    
    @classmethod
    def _on_class_call( cls, *args, **kwargs ):
        return ClassCallOverridableMeta._on_class_call( cls, *args, **kwargs )


TSelf = TypeVar( "TSelf", bound = "Coercible" )


class Coercible:
    def coerce( self: TSelf, other ) -> TSelf:
        """
        Coerce an object `other` to this type.
        
        :param other:           Object to coerce to type    
        :return:                Object of type `TSelf` 
        :exception TypeError:   Coercion not supported.
        """
        if isinstance( other, type( self ) ):
            return other
        
        r = self._on_coerce( other )
        
        if r is None:
            raise exception_helper.type_error( "type-coercion", other )
        
        return r
    
    
    def _on_coerce( self: TSelf, other: object ) -> Optional[TSelf]:
        """
        Handles `coerce`.
        
        The derived class should return an object of type `TSelf` reflecting
        the `other`. If it is unable to do so, it may return `None`.
        
        Note that the type of `other` is never `TSelf`, this is handled
        by `coerce`.
        """
        raise NotImplementedError( "abstract" )
