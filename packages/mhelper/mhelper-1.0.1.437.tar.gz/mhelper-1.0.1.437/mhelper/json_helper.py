"""
Uses type annotations to serialise and deserialse objects to/from JSON and,
unlike jsonpickle, doesn't require the type information to be part of the JSON.

To deserialise, a "serialisable annotation" should be specified, denoting the
type of object to deserialise the JSON data into. 

Viable serialisable annotations include:

* One of the basic JSON types: `int`, `str`, `float`, `bool`.
* A generic `List[T]`, `Tuple[T, ...]`, `Set[T]` or `FrozenSet[T]`.
  * The generic type `T` must itself be a serialisable annotation.
  * Note that non-generic list treated the same as the generic version with an
    `object` argument, e.g. `list` becomes `List[object]` (implicit mode only).
  * JSON: `list`.
  * Python: As per the generic, i.e. `list`, `tuple`, `set` or `frozenset.
* A generic mapping `Dict[str, T]`.
  * The generic type `T` must itself be a serialisable annotation.
  * Note that non-generic `dict` treated the same as the generic version with an
    `object` argument, e.g. `dict` becomes `Dict[str, object]` (implicit mode 
    only).
  * JSON: `dict`.
  * Python: `dict`.
* Any class with all fields annotated and each field is itself annotated with
  another serialisable annotation (see below).
  * Any unannotated field is considered to be an `object` (implicit mode only).
  * JSON: `dict`.
  * Python: As annotation
* Any class with a static `from_json` method.
  * JSON: `Any`
  * Python: As annotation
* The special annotation, `UNKNOWN`, is also permitted.
  * This will be treated as a basic JSON type, `int`, `str`, `float`, `bool`, `list` or `dict`. 
  * JSON: Any
  * Python: Same as JSON

Example annotated class:

  class MyObject:
        my_number : int
        my_text : str
        my_list : List[str]  
  
Serialisation
-------------

Serialisable annotations are only used during deserialisation. During
serialisation *to JSON* the type of the actual object is used as the annotation.
Objects may possess a `to_json` method to control serialisation themselves.        
"""
# !EXPORT_TO_README

import json as _json
import os
from enum import Flag

from mhelper import reflection_helper, string_helper
from mhelper.special_types import Sentinel
from typing import get_type_hints, Type, Union, TypeVar, cast, Any


try:
    from typing import get_origin, get_args, Literal
except ImportError:
    from typing_inspect import get_origin, get_args
    
    
    class _Literal:
        def __getitem__( self, item ):
            pass
    
    
    Literal = _Literal()

UNKNOWN = Sentinel( "Unknown" )

PYTHON_LIST_TYPES = { list, tuple, set, frozenset }
PYTHON_DICT_TYPES = { dict }

JSON_DATA_LIST = { list }
JSON_DATA_BASIC = { int, str, float, bool }
JSON_DATA_DICT = { dict }

T = TypeVar( "T" )
TJson = Union[list, dict, int, str, float, bool]


class EMode( Flag ):
    """
    Deserialisation flags.
    
    :cvar NONE: Treat input as JSON data.
    :cvar IMPLICIT: Implicit mode (treat missing annotations as `object`)
    :cvar FILE_NAME: Treat input as the file-name of a file containing JSON text.
    :cvar DEFAULT: If input is a file-name, and the file is not present, construct and return the default value.
    :cvar TEXT: Treat input as JSON text.
    """
    NONE = 0
    IMPLICIT = 1
    FILE_NAME = 2
    DEFAULT = 4
    TEXT = 8


def to_json( obj: object, target: object = None ) -> Union[TJson, str]:
    """
    Converts an object to JSON data.
    See module documentation for details.
    
    :param obj:      Source object.
    :param target:   Destination, one of:
                     `None` - return JSON data
                     `str` - return JSON data as `str` (text)
                     A `str` object - save JSON data to this file 
    :return: JSON data or JSON text, depending on `target`.
    """
    obj = __to_json( obj )
    
    if target is None:
        pass
    elif target is str:
        obj = _json.dumps( obj )
    elif isinstance( target, str ):
        with open( target, "w" ) as fout:
            _json.dump( obj, fout )
    else:
        raise ValueError( "target" )
    
    return obj


def __to_json( obj: object ) -> object:
    if hasattr( obj, "to_json" ):
        obj = obj.to_json()
    
    t = type( obj )
    
    if t in PYTHON_LIST_TYPES:
        return tuple( to_json( v ) for v in obj )
    elif t in JSON_DATA_BASIC:
        return obj
    elif t in PYTHON_DICT_TYPES:
        return { k: to_json( v ) for k, v in obj.items() }
    else:
        return { k: to_json( v ) for k, v in reflection_helper.get_attrs( obj ).items() }


def from_json( obj: object, type: Union[Type[T], Literal[UNKNOWN]] = UNKNOWN, explicit: bool = True, mode: EMode = EMode.NONE ) -> T:
    """
    Loads a json object.
    See module documentation for details.
    
    :param obj:       JSON data, JSON text, or a filename containing JSON text.
    :param type:      Serialisable annotation. See module documentation.
    :param explicit:  Deprecated, use mode flags instead.
    :param mode:      Mode flags.
    :return: Deserialised object. 
    """
    if mode & EMode.IMPLICIT:
        explicit = False
    
    if mode & EMode.FILE_NAME:
        assert isinstance( obj, str )
        
        if mode & EMode.DEFAULT and not os.path.isfile( obj ):
            return type()
        
        with open( obj ) as fin:
            obj = _json.load( fin )
    elif mode & EMode.TEXT:
        obj = _json.load( obj )
    
    return __from_json( obj, type, explicit, "root" )


def __from_json( json: object,
                 type_hint: object,
                 explicit: bool,
                 name: str
                 ) -> T:
    try:
        actual_type = type( json )
        
        if hasattr( type_hint, "from_json" ):
            return type_hint.from_json( json )
        
        if actual_type in JSON_DATA_LIST:
            # Incoming `list`
            # Find child element type... 
            if type_hint is UNKNOWN:
                __check_explicit( explicit )
                origin = list
                item_t = UNKNOWN
            elif type_hint is list:
                origin = type_hint
                item_t = UNKNOWN
            else:
                origin = get_origin( type_hint )
                
                if origin not in PYTHON_LIST_TYPES:
                    raise ValueError( f"Incoming `list` - expected the annotation to be one of {PYTHON_LIST_TYPES} (see `{get_origin.__qualname__}`)." )
                
                item_t = get_args( type_hint )[0]
            
            return origin( __from_json( v, item_t, explicit, f"[{i}]" ) for i, v in enumerate( json ) )
        elif actual_type in JSON_DATA_BASIC:
            # Incoming basic type
            
            if type_hint is UNKNOWN:
                __check_explicit( explicit )
            elif isinstance( type_hint, type ):
                if not isinstance( json, type_hint ):
                    raise ValueError( f"Expected `{type_hint}` but got `{actual_type}` at {name}." )
            else:
                raise ValueError( f"Invalid type hint `{type_hint}` for object `{actual_type}` at {name}." )
            
            return json
        elif actual_type in JSON_DATA_DICT:
            # Incoming mapping type
            # Could be either a plain dict or a complex object
            
            if type_hint is UNKNOWN:
                __check_explicit( explicit )
                origin = dict
                item_t = UNKNOWN
            else:
                origin = get_origin( type_hint )
                
                if origin is dict:
                    item_t = get_args( type_hint )[1]
                else:
                    item_t = None
            
            assert isinstance( json, dict )  # for PyCharm
            
            if origin is dict:
                # Simple dict
                return { k: __from_json( v, item_t, explicit, f"[{k!r}]" ) for k, v in json.items() }
            else:
                new_obj = type_hint.__new__( type_hint )
                
                # Complex object - use annotations
                new_annots = get_type_hints( cast( Any, type_hint ) )
                
                for field_name, field_json in json.items():
                    field_hint = new_annots.get( field_name, UNKNOWN )
                    field_value = __from_json( field_json, field_hint, explicit, f".{field_name}" )
                    setattr( new_obj, field_name, field_value )
                
                return new_obj
    except JsonDeserialiseError as ex:
        raise JsonDeserialiseError( ex.origin, ex.message, f"{__fmt_name( name, type_hint, actual_type )}\n{ex.name}" ) from ex.origin
    except Exception as ex:
        raise JsonDeserialiseError( ex, "Error deserialising due to an exception.", f"{__fmt_name( name, type_hint, actual_type )} <== {ex}" ) from ex


class JsonDeserialiseError( Exception ):
    def __init__( self, origin, message, name ):
        self.origin = origin
        self.message = message
        self.name = name
        super().__init__( f" * \n * {self.message}\n{name}" )


def __fmt_name( name, type_hint, actual_type ):
    return f" *     {name:<10} : {actual_type.__name__:<10} --> {string_helper.type_name( type = type_hint )}"


def __check_explicit( explicit ):
    if explicit:
        raise ValueError( f"Destination type is unknown and option `explicit` is set." )
