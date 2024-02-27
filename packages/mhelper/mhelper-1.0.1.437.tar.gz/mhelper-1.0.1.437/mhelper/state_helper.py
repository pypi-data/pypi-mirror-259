from typing import Type, Dict, TypeVar


_T = TypeVar( "_T" )


def restore_state( klass: Type[_T], state: Dict[str, object] ) -> _T:
    """
    Restores a class using a state dictionary.
    """
    obj = klass.__new__( klass )
    obj.__setstate__( state )
    return obj


def retrieve_state( obj ) -> Dict[str, object]:
    return obj.__getstate__()
