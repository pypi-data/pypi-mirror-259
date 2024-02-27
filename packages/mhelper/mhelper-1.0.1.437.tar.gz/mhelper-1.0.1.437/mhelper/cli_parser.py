import sys
from typing import Generic, TypeVar, Type, Sequence, List, Optional, Tuple, Union, Literal
from mhelper import array_helper


T = TypeVar( "T" )
U = TypeVar( "U" )

_sentinel = Literal["_sentinel"]


class CliParser:
    def __init__( self ):
        self.arguments = []
    
    
    def append( self, arg: T ) -> T:
        self.arguments.append( arg )
        return arg
    
    
    def flag( self, *args, **kwargs ) -> "FlagArg[T]":
        return self.append( FlagArg( self, *args, **kwargs ) )
    
    
    def value( self, *args, **kwargs ) -> "ValueArg[T]":
        return self.append( ValueArg( self, *args, **kwargs ) )
    
    
    def list( self, *args, **kwargs ) -> "ListArg[T]":
        return self.append( ListArg( self, *args, **kwargs ) )
    
    
    def multi_list( self, *args, **kwargs ) -> "MultiListArg[T]":
        return self.append( MultiListArg( self, *args, **kwargs ) )
    
    
    def parse( self, args = _sentinel ):
        if args is None:
            args = sys.argv[1:]
        
        names = { x: arg for arg in self.arguments for x in arg.names }
        
        c = []
        lst = [c]
        
        for arg in args:
            if arg in names:
                c = [arg]
                lst.append( (names[arg], c) )
            else:
                c.append( arg )
        
        for arg, values in lst:
            arg.parse( values )


class ParseError( Exception ):
    pass


class CliArgument:
    """
    The basic form of all CLI arguments is:
    
        (--arg (value * Nv)) * Na 
        
    e.g.
    
        A single value:      Nv=1    Na=1
        An optional value:   Nv=1    Na=0..1 | Nv=0..1, Na=1
        A list:              Nv=1..  Na=1
        Multiple lists:      Nv=1..  Na=1..
    """
    
    __slots__ = ("names",
                 "owner",
                 "val_cast",
                 "vals_min",
                 "vals_max",
                 "vals_default",
                 "arg_default",
                 "arg_min",
                 "arg_max",
                 "_value")
    
    
    def __init__( self,
                  owner: CliParser,
                  name: Tuple[str, ...],
                  val_cast: Type,
                  vals_default: Optional[Tuple[str, ...]],
                  vals_min: int,
                  vals_max: Optional[int],
                  arg_default: Optional[Tuple[Tuple[str, ...]]],
                  arg_min: int = 0,
                  arg_max: Optional[int] = None,
                  ):
        """
        :param owner:        Owning parser
                            
        :param name:         Name (str) or names (str, ...) of the argument.
                            
        :param val_cast:     Cast applied to each value (from `str`).
        
                             .. hint::
                             
                                 This may be a function if an assertion is
                                 desired. A `ParseError` should ideally be
                                 raised should such the assertion fail, though
                                 any exception is permitted.

        :param vals_default: List of values assumed if an argument is provided with
                             *no* values.
                             This may violate any `min`/`max` constraints if desired.

        :param vals_min:     Minimum Nv (number of values taken by the argument).
                             (Note that 0 (and 0 only) is always permitted if `default` is specified).
                            
        :param vals_max:     Maximum Nv (number of values taken by the argument).
                             `None` for no limit.
         
        :param arg_min:      Minimum number of times the argument may be specified.
                             (Note that 0 (and 0 only) is always permitted if `arg_default` is specified).
                            
        :param arg_max:      Maximum number of times the argument may be specified. 

        :param arg_default:  List of value lists assumed if the argument is *never*
                             provided.
                             This may violate any `arg_min`/`arg_max` constraints if desired.
        """
        self.names: Tuple[str, ...] = (name,) if isinstance( name, str ) else name
        self.owner: CliParser = owner
        self.val_cast: Type = val_cast
        self.vals_min: int = vals_min
        self.vals_max: Optional[int] = vals_max
        self.vals_default: Optional[Tuple[str, ...]] = vals_default
        self.arg_default: Optional[Tuple[Tuple[str, ...]]] = arg_default
        self.arg_min: int = arg_min
        self.arg_max: Optional[int] = arg_max
        self._value: List[T] = []
    
    
    def _get_value( self ):
        self.owner.parse()
        return self._value
    
    
    def error( self, message ):
        raise ParseError( f" {message}" )
    
    
    def _parse( self, values: Sequence[str] ):
        if not values:
            if self.vals_default is not None:
                self._value.append( self.vals_default )
            
            return
        
        if len( values ) < self.vals_min:
            if self.vals_min == 1:
                raise self.error( f"Error reading argument '{self}'. At least one value is expected, but {len( values )} have been provided." )
            else:
                raise self.error( f"Error reading argument '{self}'. At least {self.vals_min} values are expected, but {len( values )} have been provided." )
        
        if self.vals_max is not None and len( values ) > self.vals_max:
            if self.vals_max:
                raise self.error( f"Error reading argument '{self}'. At most {self.vals_min} values are expected, but {len( values )} have been provided." )
            else:
                raise self.error( f"Error reading argument '{self}'. No values are expected, but {len( values )} have been provided." )
        
        sequence = []
        
        for value in values:
            try:
                sequence.append( self.val_cast( value ) )
            except Exception as ex:
                raise self.error( f"Error reading argument '{self}'. At least one value provided isn't valid ({value!r}, due to the error: {ex})" ) from ex
        
        self._value.append( sequence )
    
    
    def _parsed( self ):
        if not self._value and self.arg_default is not None:
            self._value.extend( self.arg_default )
            return
        
        if len( self._value ) < self.arg_min:
            raise self.error( f"The '{self}' argument is required." )
        
        if self.arg_max is not None and len( self._value ) > self.arg_max:
            if self.arg_min == 1:
                raise ParseError( f"The '{self}' argument has been specified more than once." )
            else:
                raise ParseError( f"The '{self}' argument has been specified {len( self._value )} times. This argument should not be specified more than {self.arg_max} times." )


class FlagArg( CliArgument, Generic[T] ):
    __slots__ = ()
    
    
    def __init__( self,
                  owner: CliParser,
                  name: Tuple[str, ...],
                  cast: Type[T] = bool,
                  on: T = True,
                  off: T = False,
                  inverse: bool = False ):
        if inverse:
            on, off = off, on
        
        super().__init__( owner,
                          name,
                          val_cast = cast,
                          vals_min = 0,
                          vals_max = 0,
                          vals_default = (on,),
                          arg_min = 1,
                          arg_max = 1,
                          arg_default = ((off,),),
                          )
    
    
    def get_value( self ) -> T:
        return array_helper.one( array_helper.one( self._get_value() ) )


class ListArg( CliArgument, Generic[T] ):
    __slots__ = ()
    
    
    def __init__( self,
                  owner: CliParser,
                  name: Union[str, Tuple[str, ...]],
                  min: int = 0,
                  max: Optional[int] = None,
                  cast: Type[T] = str,
                  missing: Optional[Tuple[T, ...]] = None,
                  auto: Optional[Tuple[T, ...]] = None
                  ):
        super().__init__( owner = owner,
                          name = name,
                          vals_min = min,
                          vals_max = max,
                          val_cast = cast,
                          arg_default = (missing,),
                          vals_default = auto,
                          arg_min = 1,
                          arg_max = 1 )
    
    
    def get_value( self ) -> Sequence[T]:
        return array_helper.one( self._get_value() )


class MultiListArg( CliArgument, Generic[T] ):
    __slots__ = ()
    
    
    def __init__( self,
                  owner: CliParser,
                  name: Union[str, Tuple[str, ...]],
                  min: int = 0,
                  max: Optional[int] = None,
                  cast: Type[T] = str,
                  missing: Optional[Tuple[Tuple[T, ...], ...]] = None,
                  auto: Optional[Tuple[T, ...]] = (),
                  arg_min: int = 0,
                  arg_max: Optional[int] = None,
                  ):
        super().__init__( owner = owner,
                          name = name,
                          vals_min = min,
                          vals_max = max,
                          val_cast = cast,
                          arg_default = missing,
                          vals_default = auto,
                          arg_min = arg_min,
                          arg_max = arg_max )
    
    
    def get_value( self ) -> Sequence[Sequence[T]]:
        return self._get_value()


class ValueArg( CliArgument, Generic[T] ):
    __slots__ = ()
    
    
    def __init__( self,
                  owner,
                  name,
                  cast: Type[T] = str,
                  missing: Union[T, _sentinel] = _sentinel,
                  auto: Union[T, _sentinel] = _sentinel ):
        super().__init__( owner = owner,
                          name = name,
                          vals_min = 1,
                          vals_max = 1,
                          val_cast = cast,
                          arg_default = ((missing,),) if missing is not _sentinel else None,
                          vals_default = (auto,) if auto is not _sentinel else None,
                          arg_min = 1,
                          arg_max = 1
                          )
    
    
    def get_value( self ) -> T:
        return array_helper.one( array_helper.one( self._get_value() ) )
