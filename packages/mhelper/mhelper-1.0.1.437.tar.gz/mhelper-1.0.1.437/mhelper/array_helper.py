"""
This package includes a variety of utility functions for dealing with arrays
(lists, tuples, iterables, etc.)
"""
# !EXPORT_TO_README
import inspect
import itertools
import operator
import random
import types
import warnings
from collections import defaultdict
from itertools import chain
from typing import List, Optional, Iterator, overload, Tuple, Dict, Iterable, Union, TypeVar, Callable, Sequence, Type, Collection, Reversible, Generic, Set

import math

from mhelper import exception_helper
from mhelper.special_types import NOT_PROVIDED, Sentinel


T = TypeVar( "T" )
U = TypeVar( "U" )
V = TypeVar( "V" )
TArray = TypeVar( "TArray" )

__array_helper_sentinel = Sentinel( "__array_helper_sentinel" )


def list_type( the_list: List[T] ) -> Type[T]:
    """
    Determines the type of elements in a list

    Errors if the list doesn't contain any elements, or if the elements are of varying type

    :param the_list:    List to check
    :return:            Type of elements in the list
    """
    
    t = None
    
    for e in the_list:
        et = type( e )
        
        if t is None:
            t = et
        elif t is not et:
            raise ValueError( "Calling list_type on a list with at least two types ({0} and {1})".format( t, et ) )
    
    if t is None:
        raise ValueError( "Calling list_type on a list with no elements." )
    
    return t


def as_sequence( contents: Union[List[T], Tuple[T], T],
                 cast: Type[Iterable[T]] = None,
                 elemental_none: bool = True,
                 sequence_types: Sequence[Type[Iterable[T]]] = (tuple, list),
                 element_types: Sequence[Type] = (str,)
                 ) -> Union[List[T], Tuple[T]]:
    """
    Converts the `contents` to the specified type of sequence.
    
    .. note::
    
        The type `TArray` below is a suitable array type, from the first
        available from `cast`, `sequence_types[0]`, `tuple`.
    
    :param contents:        The input.
    
    :param elemental_none:  Controls how a `None` input is handled.
    
                            When set a `None` input is converted to an empty
                            array.
    
    :param sequence_types:  Controls how arrays are identified.
    
                            If the input is *not* one of these types, the input
                            will be converted into an array (of type `TArray`) 
                            containing the input as its sole item.
                            
                            No conversion is performed if this is not set.
    
    :param element_types:   Controls how arrays are identified.
    
                            If the input *is* one of these types, the input
                            will be converted into a array (of type `TArray`)
                            containing the input as its sole item.
                            
                            No conversion is performed if this is not set.
                             
    
    :param cast:            Controls the output.
                            
                            The result is cast to this type, if it isn't
                            already of this type.
                            
                            If this is `None`, no conversion is performed, so
                            the output could be of any of the `sequence_types`.
    
    :return: The result.
    """
    t_array: Type = cast if cast else sequence_types[0] if sequence_types else tuple
    
    if elemental_none and contents is None:
        contents = tuple()
    
    if element_types and any( isinstance( contents, x ) for x in element_types ):
        contents = t_array( (contents,) )
    
    if sequence_types and not any( isinstance( contents, x ) for x in sequence_types ):
        contents = t_array( (contents,) )
    
    if cast is not None and not isinstance( contents, cast ):
        contents = cast( contents )
    
    return contents


def to_sequence( value, cast: Union[Type[T], Dict[Type, Union[Type[T], Callable[[object], T]]]] = tuple ) -> T:
    """
    Converts `value` to `cast`.
    
    :param value:   Source value. 
    :param cast:    Map of types to destination types or expressions.
                    A single type will use the default mapping. 
    """
    if not isinstance( cast, dict ):
        my_type = cast  # closure 
        cast = { list               : my_type,
                 tuple              : my_type,
                 str                : lambda x: my_type( (x,) ),
                 types.GeneratorType: my_type,
                 None               : lambda x: my_type( (x,) ) }
    
    for src, dst in cast.items():
        if src is None or isinstance( value, src ):
            if dst is None:
                return value
            
            return dst( value )
    
    raise ValueError( f"Cannot map value to sequence because the source type is not supported. Value: {value}. Type: {type( value ).__qualname__}. Cast: {cast}." )


# !has test case
def create_index_lookup( source: Iterable[T] ) -> Dict[T, int]:
    """
    Creates a lookup table (`dict`) that allows the index of elements in
    `the_list` to quickly be found.
    """
    result = { v: i for i, v in enumerate( source ) }
    
    return result


def deinterleave_as_two( source: Iterable[T] ) -> Tuple[List[T], List[T]]:
    """
    Deinterleaves a source list, returns two new lists
    """
    dest_a = []
    dest_b = []
    iterator = iter( source )
    
    for a in iterator:
        dest_a.append( a )
        dest_b.append( next( iterator ) )
    
    return dest_a, dest_b


def deinterleave_as_iterator( source: Iterable[T] ) -> Iterator[Tuple[T, T]]:
    """
    Deinterleaves a source list, returns an iterator over tuples
    """
    iterator = iter( source )
    
    for a in iterator:
        yield a, next( iterator )


def deinterleave_as_list( source: Iterable[T] ) -> List[Tuple[T, T]]:
    """
    Deinterleaves a source list "A,B,A,B,...", returns a list of tuples "A, B"
    """
    dest_a = []
    iterator = iter( source )
    
    for a in iterator:
        dest_a.append( (a, next( iterator )) )
    
    return dest_a


def deinterleave_as_dict( source: Iterable[T] ) -> Dict[T, T]:
    """
    Deinterleaves a source list "K,V,K,V,...", returns a dictionary "D" of "V = D[K]"
    """
    return dict( deinterleave_as_iterator( source ) )


def has_any( sequence: Iterable ) -> bool:
    """
    Returns if the iterable contains _any_ elements (i.e. non-zero length).
    """
    for _ in sequence:
        return True
    
    return False


def iterate_descendants( root: T, fn: Callable[[T], Iterable[T]] = None ) -> Iterator[T]:
    """
    Iterates all items and descendants.
    
    :param root:    Where to start 
    :param fn:      How to get the children 
    :return:        Iterator over items and all descendants 
    """
    if fn is None:
        fn = lambda x: x
    
    for x in fn( root ):
        yield x
        yield from iterate_descendants( x, fn )


def ensure_capacity( array: List[T], index: int, value: T = None, dynamic = None ) -> None:
    """
    Pads `value` into the `array` to ensure `index` can be accessed.
    """
    if dynamic is not None:
        while len( array ) <= index:
            array.append( dynamic() )
    else:
        if len( array ) <= index:
            needed = index + 1 - len( array )
            array.extend( [value] * needed )


def index_of_first( array: Iterable[T], predicate: Callable[[T], bool], default = None ) -> Optional[int]:
    """
    Returns the index of the first element in the `array` matching the
    `predicate`.
    """
    for i, e in enumerate( array ):
        if predicate( e ):
            return i
    
    return exception_helper.default( default )


class Indexer:
    """
    Provides a name to index and index to name lookup table.
    
    Note that `Indexer` has no indexer - be specific, use:
        `Indexer.name`
        `Indexer.index`
    """
    __slots__ = "indexes", "names"
    
    
    def __init__( self, iterator: Iterable[object] = None ):
        """
        CONSTRUCTOR
        Allows initialisation from existing entries
        """
        self.indexes = { }  # names to indices
        self.names = []  # indices to names
        
        if iterator is not None:
            for name in iterator:
                self.add( name )
    
    
    def add( self, name: object ):
        """
        Adds a new name with a new index.
        """
        index = self.indexes.get( name )
        
        if index is not None:
            return index
        
        index = len( self )
        
        self.indexes[name] = index
        self.names.append( name )
        
        return index
    
    
    def __len__( self ) -> int:
        """
        !OVERRIDE
        Obtains the number of names
        """
        return len( self.names )
    
    
    def index( self, name: object ) -> int:
        """
        Obtains the index of the specified name.
        """
        return self.indexes[name]
    
    
    def name( self, index: int ):
        """
        Obtains the name at the specified index.
        """
        return self.names[index]


def first( array: Iterable[T], default ) -> Optional[T]:
    """
    Returns the first element of the `array`, using the `default` if the array
    is empty.
    """
    return single( array, empty = default, multi = FIRST )


def first_or_none( array: Iterable[T], default = None ) -> Optional[T]:
    """
    Returns the first element of the `array`, using the `default` if the array
    is empty.
    """
    return single( array, empty = default, multi = FIRST )


def first_or_error( array: Iterable[T] ) -> T:
    """
    Returns the first element of the `array`, raising a `KeyError` if the array
    is empty.
    """
    return single( array, multi = FIRST )


def single_or_none( array: Iterable[T], default = None ) -> Optional[T]:
    """
    Returns the single element in the `array`, returning the `default` if there
    are 0 or more than 1 elements.
    """
    return single( array, empty = default, multi = default )


def single_or_error( array: Iterable[T] ) -> T:
    """
    Returns the first element of the array, raising a `KeyError` if the length
    is not `1`.
    
    :except KeyError: Raised if the length is not 1.
    """
    return single( array )


FIRST = Sentinel( "(First)" )


@overload
def single( array: Iterable[T], empty: Sentinel = NOT_PROVIDED, multi: Sentinel = NOT_PROVIDED ) -> T:
    pass


@overload
def single( array: Iterable[T], empty: Union[Sentinel, U] = NOT_PROVIDED, multi: Union[Sentinel, U] = NOT_PROVIDED ) -> Optional[T]:
    pass


def single( array: Iterable[T], empty: U = NOT_PROVIDED, multi: U = NOT_PROVIDED ) -> Union[T, U]:
    """
    Returns the first element of the array.
    
    Handling of empty, or multi-element arrays is controlled via parameters,
    the default behaviour is to raise a `KeyError` if the array length is not
    `1`.
    
    :param array:       Array
    :param empty:       Default value if the array is empty.
                        If `NOT_PROVIDED` a `KeyError` is raised.
    :param multi:       Default value if the array has more than one element.
                        If `NOT_PROVIDED` a `KeyError` is raised.
                        If `FIRST` the first element is returned even if there are multiple elements.
    :return:            First element or the default.
    :except KeyError:   Not able to retrieve first element 
    """
    from mhelper import string_helper
    it = iter( array )
    
    try:
        first = next( it )
    except StopIteration:
        if empty is NOT_PROVIDED:
            raise KeyError( "Cannot extract the single element of the iterable because the iterable has no elements: {}".format( repr( array ) ) )
        else:
            return empty
    
    if multi is FIRST:
        return first
    
    try:
        next( it )
        
        if multi is NOT_PROVIDED:
            raise KeyError( "Cannot extract the single element of the iterable because the iterable has multiple elements: {}".format( string_helper.format_array( array, limit = 10 ) ) )
        else:
            return multi
    except StopIteration:
        return first


one = single


def md_single( array: Iterable[Iterable[T]], dimensions = 2 ) -> Optional[T]:
    for dimension in range( dimensions ):
        array = single( array )
    
    return array


def lagged_iterate( sequence: Iterable[Optional[T]], head = False, tail = False ) -> Iterator[Tuple[Optional[T], Optional[T]]]:
    """
    Yields all adjacent pairs in the sequence. 
    
    :param sequence:        Sequence to iterate over `(0, 1, 2, 3, ..., n)` 
    :param head:            Include the head element `(None, 0)`. (off by default) 
    :param tail:            Include the tail element `(n, None)`. (off by default)
    :return:                The iteration: `(0,1), (1,2), (2,3), (...,...), (n-1,n)`
    
                                `head`  `tail`      `result when sequence = (1)`     `result when sequence = (1, 2, 3)`
                                False   False                                                   (1, 2), (2, 3)
                                True    False       (None, 1)                        (None, 1), (1, 2), (2, 3)  
                                True    True        (None, 1) (1, None)              (None, 1), (1, 2), (2, 3), (3, None)
                                False   True                  (1, None)                         (1, 2), (2, 3), (3, None)
                                
    """
    has_any = 0
    previous = None
    
    for current in sequence:
        if has_any:
            yield previous, current
        elif head:
            yield None, current
        
        has_any += 1
        previous = current
    
    if tail:
        yield previous, None


def lagged_iterate_3( sequence: Iterable[Optional[T]], missing = None ) -> Iterator[Tuple[Optional[T], T, Optional[T]]]:
    """
    Yields a tuple of (previous)-(current)-(next) for each element of the sequence.
    
    :param sequence:    Sequence to iterate 
    :param missing:     Value to use as the previous or next when there is no such element (i.e. the element before the first or after the last) 
    :return:    Iterator[...]:
                    [...] Tuple[3]:
                            [0] previous (or `missing`)
                            [1] current
                            [2] (or `missing`) 
    """
    nm1 = missing
    nm2 = None
    
    for index, nm0 in enumerate( sequence ):
        if index:
            yield nm2, nm1, nm0
        nm2 = nm1
        nm1 = nm0
    
    yield nm2, nm1, missing


def triangular_comparison( sequence: List[T] ) -> Iterator[Tuple[T, T]]:
    """
    Order independent yielding of every element vs every other element.
    
    Pairs are only listed once, so if (A,B) is yielded, (B,A) is not.
    Self comparisons (A,A) are never listed.
    
    Unlike `itertools.combinations` this function guarantees that
    ``result[0].index < result[1].index``.
    """
    for index, alpha in enumerate( sequence ):
        for beta in sequence[index + 1:]:
            yield alpha, beta


def square_comparison( sequence: List[T] ) -> Iterator[Tuple[T, T]]:
    """
    Order dependent yielding of every element vs every other element.
    
    Pairs are listed, so if (A,B) is yielded, so will (B,A).
    Self comparisons (A,A) are never listed.
    """
    for index, alpha in enumerate( sequence ):
        for beta in sequence[:index]:
            yield alpha, beta
        
        for beta in sequence[index + 1:]:
            yield alpha, beta


def ordered_insert( list: List[T], item: T, key: Callable[[T], object] ):
    """
    Inserts the `item` into the `list` that has been sorted by `key`.
    """
    import bisect
    list.insert( bisect.bisect_left( [key( x ) for x in list], key( item ) ), item )


def average( list: Iterable ) -> float:
    """
    Returns the mean average of the values in the list.
    """
    return sum( list ) / count( list )


def count( list: Collection ) -> int:
    """
    Returns the number of items in the iterable.
    
    :param list: 
    :return: 
    """
    try:
        return len( list )
    except Exception:
        return sum( 1 for _ in list )


def when_last( i: Iterable[T] ) -> (T, bool):
    f = True
    l = None
    
    for x in i:
        if not f:
            yield l, False
        else:
            f = False
        
        l = x
    
    yield l, True


def when_first_or_last( iterable: Iterable[T] ) -> (T, bool, bool):
    """
    Like `enumerate`, returning the tuple: (enumerator), (is first element), (is last element).
    """
    is_first = True
    last_item = None
    has_yielded_first = True
    
    for item in iterable:
        if not is_first:
            yield last_item, has_yielded_first, False
            has_yielded_first = False
        else:
            is_first = False
        
        last_item = item
    
    if not is_first:
        yield last_item, has_yielded_first, True


def find( iterable: Iterable[T], predicate: Callable[[T], bool], default = NOT_PROVIDED ) -> T:
    """
    Finds the item in the `iterable` that matches the `predicate` and returns it.
    :param iterable: 
    :param predicate: 
    :param default: 
    :return: 
    """
    for x in iterable:
        if predicate( x ):
            return x
    
    if default is not NOT_PROVIDED:
        return default
    else:
        raise ValueError( "No such value." )


def iter_distance_range( min: int, max_: int, start: int ) -> Iterator[int]:
    yield start
    i = 1
    while True:
        if (start - i) >= min:
            yield start - i
        
        if (start + i) < max_:
            yield start + i
        
        if (start - i) < min and (start + i) >= max_:
            return
        
        i += 1


def distance_range( min: int, max_: int, start: int ) -> List[int]:
    return list( iter_distance_range( min, max_, start ) )


def add_to_listdict( dict_: Dict[T, List[U]], key: T, value: U ):
    """
    Similar to `defaultdict(list)[key].append(value)`, but for dicts that aren't
    defaultdicts.
    """
    list_ = dict_.get( key )
    
    if list_ is None:
        list_ = []
        dict_[key] = list_
    
    list_.append( value )


def remove_from_listdict( dict_: Dict[T, List[U]], key: T, value: U ):
    """
    Converse of `add_to_listdict`. The key is removed if the list becomes empty.
    """
    list_ = dict_[key]
    list_.remove( value )
    
    if len( list_ ) == 0:
        del dict_[key]


def divide_workload( total_workload: int, num_workers: int, expand: bool = False ) -> List[Tuple[int, int]]:
    """
    Divides a workload of discrete objects between workers.
    
    :param total_workload:      The total workload to divide 
    :param num_workers:         The number of workers
    :param expand:              When true, `num_workers` specifies the maximum work a single worker can do.
                                The number of workers is calculated from this. 
    :return:                    A list of tuples, denoting the start and end of each worker's portion.
                                `len(result)` is thus the number of workers.
    """
    if expand:
        num_workers = int( 0.5 + total_workload / num_workers )
    
    r = []
    
    for index in range( num_workers ):
        r.append( get_workload( index, total_workload, num_workers ) )
    
    return r


def get_workload( index: int, total_workload: int, num_workers: int ) -> Tuple[int, int]:
    """
    Divides a workload of discrete objects between workers, and obtains the specified worker's portion.
    
    :param index:               The index 'i' of the worker to acquire the workload for. 
    :param total_workload:      The total workload 
    :param num_workers:         The number of workers 
    :return:                    A tuple denoting the start and end of the i'th worker's portion. 
    """
    worker_size = total_workload / num_workers
    
    start = index * worker_size
    
    if index == num_workers - 1:
        end = total_workload
    else:
        end = int( start + worker_size )
    
    return int( start ), end


def batch_list( work: Sequence, batch_size: int ):
    """
    Divides a list of `work` into lists of size `batch_size`.
    (The final element may be shorter than the rest - use `batch_distribute` for distributed batches).
    """
    return [work[i:i + batch_size] for i in range( 0, len( work ), batch_size )]


def batch_distribute_list( list_: Sequence[T], *args, **kwargs ) -> List[Sequence[T]]:
    """
    Variant of `batch_distribute` that returns list slices rather than sizes.
    """
    sizes = batch_distribute( work = len( list_ ), *args, **kwargs )
    r: List[Sequence[T]] = []
    start = 0
    
    for size in sizes:
        end = start + size
        r.append( list_[start: end] )
        start = end
    
    return r


def batch_distribute( work: int, min_batch: int = None, max_batch: int = None ) -> List[int]:
    """
    Divides a workload as evenly as possible.
    One, and only one, of `min_batch` or `max_batch` must be specified.
    
    :param work:            Number of items 
    :param min_batch:       Min size of batch 
    :param max_batch:       Max size of batch 
    :return:                Array of batch sizes (i.e. work per worker). 
    """
    if max_batch is not None:
        if min_batch is not None:
            raise ValueError( "Specify `min_batch` or `max_batch`, but not both." )
        
        if max_batch > work:
            return [work]
        
        batch_size = max_batch
        operator = math.ceil
    elif min_batch is not None:
        batch_size = min_batch
        operator = math.floor
    else:
        assert False
    
    if batch_size > work:
        raise ValueError( "It is impossible to distribute this workload." )
    
    workers_req = work / batch_size
    workers = operator( workers_req )
    actual_batch_size = work // workers if workers else 0
    missing = work - (actual_batch_size * workers)
    
    r = []
    
    for n in range( workers ):
        if n < missing:
            r.append( actual_batch_size + 1 )
        else:
            r.append( actual_batch_size )
    
    return r


def cross( l: Iterable[T] ) -> Iterator[Tuple[T, T]]:
    """
    Yields every item in the list `v` against every other item in the list.
    Items are not self crossed, so 1, 2, 3 does not yield 1 v 1.
    Items are only crossed once, so 1, 2, 3 yields 1 v 2 but not 2 v 1.
    
    :param l:   The source iterator. This must yield the elements in the same order each time it is called.
                A special handler is in place for `set` however. 
    """
    warnings.warn( "Deprecated - use itertools.combinations/permutations", DeprecationWarning )
    
    if isinstance( l, set ):
        l = list( l )
    
    for a in l:
        for b in l:
            if b is a:
                break
            
            yield a, b


def make_dict_list( sequence: Iterator[Tuple[T, U]], target = None ) -> Dict[T, List[U]]:
    """
    For a sequence of keys and values, where keys may be repeated, creates a
    dictionary of lists.
    """
    if target is None:
        target = { }
    
    for k, v in sequence:
        l = target.get( k )
        
        if l is None:
            l = []
            target[k] = l
        
        l.append( v )
    
    return target


def group_by( sequence: Iterable[T], key: Callable[[T], U], target = None ) -> Dict[U, List[T]]:
    """
    Puts items into boxes.
    """
    return make_dict_list( ((key( x ), x) for x in sequence), target = target )


def apply_by( sequence: Iterable[T], key: Callable[[T], U], fun: Callable[[List[T]], V] ) -> Dict[U, V]:
    """
    Same as `group_by`, then executes a method, `fun`, on each list.
    """
    d = group_by( sequence, key )
    return { k: fun( v ) for k, v in d.items() }


box = group_by


def remove_where( source: List[T], predicate: Callable[[T], bool] ) -> None:
    """
    Removes all items from a `source` list matching the `predicate`.
    """
    for i in range( len( source ) - 1, -1, -1 ):
        if predicate( source[i] ):
            del source[i]


def list_ranges( l ):
    return list( get_ranges( l ) )


def get_ranges( l ):
    l = sorted( l )
    
    s = None
    li = None
    
    for i in l:
        if i - 1 == li:
            li = i
            continue
        else:
            if s is not None:
                yield s, li
            s = i
            li = i
    
    yield s, li


def is_simple_iterable( v ) -> bool:
    return isinstance( v, list ) \
           or isinstance( v, tuple ) \
           or isinstance( v, set ) \
           or isinstance( v, frozenset ) \
           or inspect.isgenerator( v )


def is_simple_sequence( v ) -> bool:
    return isinstance( v, list ) \
           or isinstance( v, tuple )


def get_num_combinations( n: Union[int, float, Sequence], r: int ):
    """
    Gets the number of combinations of an array without actually calculating
    the combinations.
     
    :param n:       Either the total number of elements in the array (as an
                    `int` or `float`), or the array itself (which must provide
                    a `__len__`).
    :param r:       Number of elements in each combination. 
    :return:        Number of available combinations. 
    """
    if not isinstance( n, int ) and not isinstance( n, float ):
        n = len( n )
    
    if r == n:
        return 1
    elif n < r:
        return 0
    
    return math.factorial( n ) // (math.factorial( n - r ) * math.factorial( r ))


def let( sequence: List[T], index: int, value: T = None, pad: T = None ) -> None:
    """
    Sets the `index`th element of the `sequence` to `value`,
    extending the sequence with `pad` if it is not large enough.
    
    :param sequence: 
    :param index: 
    :param value: 
    :param pad: 
    """
    if len( sequence ) <= index:
        sequence.append( pad )
    
    sequence[index] = value


class KeyedSet( Generic[T] ):
    """
    A dictionary in which the key and value are the same.
    
    By specifying a `key`, this can also be used as a dictionary with a
    predefined key accessor.
    """
    __slots__ = "__key_fn", "__contents"
    
    
    def __init__( self, key = None ):
        if key is None:
            key = lambda x: x
        
        self.__key_fn = key
        self.__contents = dict()
    
    
    def __len__( self ) -> int:
        return len( self.__contents )
    
    
    def __iter__( self ) -> Iterator[T]:
        return iter( self.__contents )
    
    
    def keys( self ) -> Iterable[T]:
        return self.__contents.keys()
    
    
    def add( self, item: T ) -> None:
        self.__contents[self.__key_fn( item )] = item
    
    
    def remove( self, item: T ) -> None:
        del self.__contents[self.__key_fn( item )]
    
    
    def __getitem__( self, item: T ) -> T:
        return self.__contents[self.__key_fn( item )]


def get_index( options: Iterable[T], value: T, default = NOT_PROVIDED ) -> int:
    """
    Equivalent to `list.index`, but works on any iterable.
    """
    for index, option in enumerate( options ):
        if option == value:
            return index
    
    if default is NOT_PROVIDED:
        raise KeyError( value )
    else:
        return default


def list_setdefault( a: List[T],
                     value: Union[T, Callable[[T], bool]],
                     default: Union[T, Callable[[], T]] ) -> T:
    if not callable( value ):
        value = value.__eq__
    
    for item in a:
        if value( item ):
            return item
    
    if callable( default ):
        default = default()
    
    a.append( default )


class WriteOnceDict( dict ):
    """
    A `dict` wrapper with built in checking than ensures each `key` is only set
    once.
    """
    __slots__ = "__frozen",
    
    
    def __init__( self, seq = None ):
        self.__frozen = False
        
        if seq is None:
            super().__init__()
            return
        
        # Special case if not a dict - check for duplicates
        if not isinstance( seq, dict ):
            super().__init__()
            
            for key, value in seq:
                self[key] = value
            
            return
        
        super().__init__( seq )
    
    
    def freeze( self ):
        self.__frozen = True
    
    
    @property
    def is_frozen( self ):
        try:
            # During deserialisation the dict will get deserialised *before*
            # the frozen flag
            return self.__frozen
        except AttributeError:
            self.__frozen = False
            return False
    
    
    def __setitem__( self, key, value ):
        if self.is_frozen:
            raise ValueError( "Dictionary is frozen, cannot accept a new value." )
        
        if key in self:
            return self.handle_duplicate( key, value )
        
        super().__setitem__( key, value )
    
    
    def handle_duplicate( self, key, value ):
        raise ValueError( f"WriteOnceDict key already in use, cannot accept new value.\n"
                          f"* Key: {key!r}\n"
                          f"* Existing value: {self[key]!r}\n"
                          f"* New value: {value!r}" )
    
    
    def update( self, E = None, **F ):
        if E is not None:
            for key, value in E.items():
                self[key] = value
        
        if F is not None:
            for key, value in F.items():
                self[key] = value


class DefaultList:
    """
    A `list` that pads with a `default` value if the available index is
    unavailable.
    """
    __slots__ = "default", "data"
    
    
    def __init__( self, default ):
        self.default = default
        self.data = []
    
    
    def __getitem__( self, item ):
        while len( self.data ) <= item:
            self.data.append( self.default() )
        
        return self.data[item]
    
    
    def __iter__( self ):
        return iter( self.data )
    
    
    def __len__( self ):
        return len( self.data )


def transpose( matrix: Iterable[Iterable[object]] ):
    """
    Transposes a `matrix`.
    
    :param matrix: A `matrix`, represented as a `list` of `list`\s. 
    :return: A new `list` of `list`\s, representing the transposed matrix. 
    """
    return list( zip( *matrix ) )


def check_list( aa, bb, eq = lambda a, b: a == b ):
    aa = list( aa )
    bb = list( bb )
    
    if len( aa ) != len( bb ):
        return False
    
    for a in aa:
        for i, b in enumerate( bb ):
            if eq( a, b ):
                del bb[i]
                break
        else:
            return False
    
    return True


def find_duplicate( xx ):
    y = set()
    
    for x in xx:
        if x in y:
            return x
        else:
            y.add( x )
    
    return None


def assert_no_duplicates( values, name = "value" ):
    y = set()
    
    for x in values:
        if x in y:
            raise ValueError( "At least one duplicate {} '{}' is present in the list: {}.".format( name, x, values ) )
        else:
            y.add( x )
    
    return None


def sum_using( x, fn = lambda x, y: x + y ):
    first = True
    r = None
    
    for y in x:
        if first:
            first = False
            r = y
        else:
            r = fn( r, y )
    
    return r


def merge_dicts( *args ):
    """
    Combines multiple dictionaries.
    Later keys take precedence.
    """
    r = { }
    
    for dic in args:
        assert isinstance( dic, dict )
        r.update( dic )
    
    return r


def add_to_lookup( dictionary: Dict[object, int], key: object ) -> int:
    """
    Gets the key from the dictionary, or creates it with length of the 
    dictionary if it is missing. The new or existing value is returned.
    
    This is useful for instance to assign colours to unique values in plots::
    
        values = ["alice", "bob", "charlie", "bob"]
        tmp = {}
        colours = [add_to_lookup(tmp, value) for value in values]
        # --> colours = [0, 1, 2, 1] 
    """
    return dictionary.setdefault( key, len( dictionary ) )


class UniqueIndexer:
    def __init__( self ):
        self.data = { }
    
    
    def __getitem__( self, item: object ) -> int:
        return self.data.setdefault( item, len( self.data ) )


class SetDifference:
    """
    Calculates the differences beteen two sets.
    """
    
    
    def __init__( self, a, b, a_name = "a", b_name = "b" ):
        self.a = frozenset( a )
        self.b = frozenset( b )
        self.a_only = self.a - self.b
        self.b_only = self.b - self.a
        self.a_name = a_name
        self.b_name = b_name
        self.is_different = bool( self.a_only or self.b_only )
    
    
    def __bool__( self ):
        return self.is_different
    
    
    def __repr__( self ):
        if self.is_different:
            return f"{self.a_name}-only: {self.a_only}. {self.b_name}-only: {self.b_only}."
        else:
            return "Sets are the same."


def rank_tie( array: Sequence, reverse = False, ne = operator.ne ) -> List[int]:
    """
    As `order`, but accounts for identical values::
    
        rank_tie("CABC") --> 2 0 1 2
    
    Elements of array are compared for equality against the previous ranked using `eq`.
    
    :result: Ranks of array (0-based), in array order.
    """
    r = [-1] * len( array )
    
    previous = __array_helper_sentinel
    current_rank = None
    
    for rank_, index in enumerate( rank( array, reverse = reverse ) ):
        current = array[index]
        
        if previous is __array_helper_sentinel or ne( current, previous ):
            current_rank = rank_
        
        r[index] = current_rank
        previous = current
    
    return r


def quantile( array: Sequence, *args, **kwargs ) -> List[float]:
    """
    As `rank_tie`, but returns the quantiles.
    """
    ranks = rank_tie( array, *args, **kwargs )
    num_subjects = len( array )
    return [rank / num_subjects for rank in ranks]


def rank( array: Sequence, reverse = False ) -> List[int]:
    """
    `rank` ranks the values, lowest first.
    `order`
    
    Assumes no identical values.
    
    Example::
    
        rank("CAB")  -->  1 2 0
        order("CAB") -->  2 0 1
    
    :result: Indexes into `array`, in rank order.
    """
    return sorted( range( len( array ) ), key = array.__getitem__, reverse = reverse )


def order( array: Sequence, reverse = False ) -> List[int]:
    """
    As `rank`, but transforms the result to be ranks in index order, rather than
    indices in rank order. See `rank` for details.
    
    i.e. C A B
    
    `rank` -->  0 1 3 2
    
    
    :result: Ranks of array (0-based), in array order. 
    """
    r = [-1] * len( array )
    
    for rank_, index in enumerate( rank( array, reverse = reverse ) ):
        r[index] = rank_
    
    return r


def assert_lut_in_order( d ):
    """
    Checks that a lookup table (LUT) was generated in the same order as its
    indices.
    
    Note that this isn't true for all LUTs, but it is necessary when we want to
    `zip` the keys back up with with whatever data it is that the LUT points to.
    """
    for i, (k, v) in enumerate( d.items() ):
        if i != v:
            raise ValueError( "A lookup table (LUT) is out of order. "
                              "This may happen on non-Cython installations where OrderedDict has not been used. "
                              "Change the program to use OrderedDict or use a standard Python install. "
                              "This problem may also occur when a LUT has been generated out of order, which is not expected in this case. "
                              f"Index: {i}\n"
                              f"Key:   {k}\n"
                              f"Value: {v}" )


def list_tree( start: T, get_children: Callable[[T], Sequence[T]], bf = True ) -> List[T]:
    """
    Lists the contents of a tree, depth or breadth first.
    
    :param start:           Root node 
    :param get_children:    Method to get children of node 
    :param bf:              Breadth first flag. 
    :return:                Tree contents, as a list. 
    """
    if bf:
        return list_tree_breadth_first( start, get_children )
    else:
        return list_tree_depth_first( start, get_children )


def list_tree_breadth_first( start: T, get_children: Callable[[T], Iterable[T]] ) -> List[T]:
    """
    Lists the full contents of a tree, breadth first.
    """
    total = []
    todo = [start]
    
    while todo:
        w = todo.pop( 0 )
        total.append( w )
        todo.extend( get_children( w ) )
    
    return total


def list_tree_depth_first( start: T, get_children: Callable[[T], Reversible[T]] ) -> List[T]:
    """
    Lists the full contents of a tree, depth first.
    """
    return list( iter_tree_depth_first( start, get_children ) )


def iter_tree_depth_first( start: T, get_children: Callable[[T], Reversible[T]] ) -> Iterator[T]:
    """
    Iterates the full contents of a tree, depth first.
    """
    todo = [start]
    
    while todo:
        w = todo.pop()
        yield w
        todo.extend( reversed( get_children( w ) ) )


class Remover:
    """
    Iterates over a list, removes flagged items only when the block ends.
    
    Usage::
    
        with Remover( my_list ) as remover:
            for item in remover:
                spam
                if eggs:
                    remover.remove()
                
    """
    __slots__ = "_array", "__iterator", "__stage", "__in_place"
    
    
    def __init__( self, array: List, in_place = True ):
        """
        !CONSTRUCTOR
        :param array:       List to use. 
        :param in_place:    When `True`, the results replace the contents of `array`.
                            When `False`, the results are stored as a new variable obtainable via `Remover.get_array()`.
        """
        self._array = array
        self.__iterator = None
        self.__stage = 0
        self.__in_place = in_place
    
    
    def __enter__( self ):
        assert self.__stage == 0, "Already in use"
        self.__stage = 1
        self.__iterator = Remover.Iterator( self )
        return self.__iterator
    
    
    def __exit__( self, exc_type, exc_val, exc_tb ):
        assert self.__stage == 1, "Not in use / already used"
        self.__stage = 2
        to_drop = set( self.__iterator.to_drop )
        
        array = [v for i, v in enumerate( self._array ) if i not in to_drop]
        
        if self.__in_place:
            self._array.clear()
            self._array.extend( array )
        else:
            self._array = array
    
    
    def get_array( self ):
        assert self.__stage == 2, "Not ready"
        return self._array
    
    
    class Iterator:
        __slots__ = "__array", "__n", "__max", "to_drop"
        
        
        def __init__( self, remover: "Remover" ):
            self.__array = remover._array
            self.__n = -1
            self.__max = len( self.__array )
            self.to_drop = []
        
        
        def __iter__( self ):
            return self
        
        
        def __next__( self ):
            self.__n += 1
            
            if self.__n < self.__max:
                return self.__array[self.__n]
            else:
                raise StopIteration()
        
        
        def drop( self ):
            self.to_drop.append( self.__n )


def _is_not_none( x ):
    return x is not None


def coalesce( *items, key = _is_not_none, default = None ):
    """
    Coalesce, returns first matching item, or None.
    
    By default this behaves as a null-coalescing operator.
    """
    for item in items:
        if key( item ):
            return item
    
    return exception_helper.default( default )


def find_all( source: Iterable[T], keys: Iterable[U], match: Callable[[T, U], bool] ) -> List[T]:
    """
    Searches a `source` list for values `match`\ing the `keys`.
    
    If a key is not found, or matches multiple entries, a `KeyError` is raised.
    """
    r: List[T] = []
    
    for key in keys:
        match_: Optional[T] = __array_helper_sentinel
        
        for subject in source:
            if match( subject, key ):
                if match_ is not __array_helper_sentinel:
                    raise KeyError( f"The key '{key}' has matched multiple subjects, at least the following two: `{match_!r}` and `{subject!r}`" )
                
                match_ = subject
        
        if match_ is __array_helper_sentinel:
            raise KeyError( f"The key '{key}' has matched no subjects." )
        
        r.append( match_ )
    
    return r


def find_all_by_lut( source: Iterable[T], find: Iterable[U], key: Union[Sequence[Callable[[T], U]], Callable[[T], object]], ) -> List[T]:
    """
    Similar to `find_all`, but creates a lookup table first, giving an error if
    a source item is represented by multiple keys (even if it isn't searched
    for).
    
    :param source:       Iterable to search
    :param find:         Iterable to search for 
    :param key:          One or more key-generating functions 
    :return:             Matched elements
    :exception KeyError: Mismatch 
    """
    if callable( key ):
        key = key,
    
    lut = { }
    
    for item in source:
        for key_fn in key:
            key_ = key_fn( item )
            
            if key_ in lut:
                raise ValueError( f"The key '{key}' maps to multiple subjects, at least the following two: `{lut[key_]!r}` and `{item!r}`" )
            
            lut[key_] = item
    
    r = []
    
    for item in find:
        try:
            r.append( lut[item] )
        except KeyError as ex:
            raise KeyError( f"Key '{item}' not found in the lookup table." ) from ex
    
    return r


def move_values_to_front( array: Iterable[T], which: Iterable[U], transform: Callable[[T], U] = None ) -> Tuple[T, ...]:
    """
    As for `move_to_front`, but uses a predicate that tests for presence of the
    `which` values (optionally `transform`\ed) in the `array`.
    """
    which = frozenset( which )
    
    if transform is None:
        predicate = which.__contains__
    else:
        predicate = lambda x: transform( x ) in which
    
    return move_to_front( array, predicate )


def move_to_front( array: Iterable[T], predicate: Callable[[T], bool] ) -> Tuple[T, ...]:
    """
    Creates a new version of `array` that contains the specified elements at the front.
    Importantly, the order of the front and back parts remains unchanged.
    
    :param array:       Source array 
    :param predicate:   Predicate for moving items to front.
    :return:            Tuple. 
    """
    front = []
    back = []
    
    for value in array:
        if predicate( value ):
            front.append( value )
        else:
            back.append( value )
    
    return tuple( chain( front, back ) )


def get_any( lut: dict, *keys, default = NOT_PROVIDED, pop = False ):
    """
    Tries to get each key in turn from the dictionary, returning the first match.
    
    :param lut:          Dictionary / lookup table 
    :param keys:         Keys to try         
    :param default:      Value returned on failure.
                         Use `NOT_PROVIDED` for error. 
    :param pop:          Remove match.
    :return:             First matching value
    :exception KeyError: No match and no default provided.    
    
    """
    for key in keys:
        value = lut.get( key, __array_helper_sentinel )
        
        if value is not __array_helper_sentinel:
            if pop:
                del lut[key]
            
            return value
    
    if default is NOT_PROVIDED:
        raise KeyError( f"None of the specified keys were found in the dictionary: {keys}" )
    
    return default


def get_path( lut: dict, *keys, default = NOT_PROVIDED ):
    """
    Gets the element from a path of dictionaries.
     
    :param lut:     Dictionary of dictionaries 
    :param keys:    Sequence of keys 
    :param default: Value to return if any element of the path does not exist.
                    If `NOT_PROVIDED` an error is raised. 
    :return:        Value of final path element.
    :exception KeyError: Path element not found and no default provided. 
    """
    for key in keys:
        try:
            lut = lut.get( key, __array_helper_sentinel )
        except:
            raise TypeError( f"The key {key!r} is not a dictionary in the dictionary path {keys!r}." )
        
        if lut is __array_helper_sentinel:
            if default is NOT_PROVIDED:
                raise KeyError( f"The key {key!r} could not be resolved in the dictionary path {keys!r}." )
            
            return default
    
    return lut


class OrderedSet( Generic[T] ):
    """
    What it says on the tin.
    
    Should behave like `Set`, but ordered.
    """
    
    
    def __init__( self, items: Optional[Iterable[T]] = None ):
        self.set: Set[T] = set()
        self.list: List[T] = list()
        
        if items:
            for item in items:
                self.add( item )
    
    
    def add( self, item: T ) -> None:
        if item in self.set:
            return
        
        self.list.append( item )
        return self.set.add( item )
    
    
    def update( self, items ):
        for item in items:
            self.add( item )
    
    
    def remove( self, item: T ) -> None:
        """
        :exception KeyError:
        """
        self.set.remove( item )
        self.list.remove( item )
    
    
    def __contains__( self, item: T ) -> bool:
        return item in self.set
    
    
    def __iter__( self ) -> Iterator[T]:
        return iter( self.list )
    
    
    def __len__( self ) -> int:
        return len( self.list )
    
    
    def __getitem__( self, item: int ) -> T:
        return self.list[item]
    
    
    def __str__( self ) -> str:
        return self.list.__str__()
    
    
    def __bool__( self ) -> bool:
        return bool( self.list )
    
    
    def __repr__( self ) -> str:
        return f"{self.__class__.__qualname__}( {self.list!r} )"


def nth( array: Iterable[T], n: int ) -> T:
    """
    Gets the nth item of the array.
    """
    for i, v in enumerate( array ):
        if i == n:
            return v
    
    raise KeyError( n )


def popin( array: List[T], *elements: T ) -> bool:
    """
    A combination of `in` and `pop` - returns if any element from `elements` is
    in the `array`, removing it from the `array` if so.
    
    If multiple elements match, only the first is removed.
    """
    for element in elements:
        if element not in array:
            continue
        
        index = array.index( element )
        del array[index]
        return True
    
    return False


_TRowKey = object
_TColKey = object
_TValue = object
_TMissing = object


def long_to_wide( array: Sequence[Sequence[Union[_TRowKey, _TColKey, _TValue]]],
                  row: int,
                  col: int,
                  val: int,
                  miss: _TMissing = None ) -> Tuple[Dict[_TRowKey, int],
                                                    Dict[_TColKey, int],
                                                    List[List[Union[_TValue, _TMissing]]]]:
    """
    Long to wide pivot
    
    :param array:   Source array, a list of sequences
    :param row:     Index of row key, in each row of the source array
    :param col:     Index of column key, in each row of the source array
    :param val:     Index of value, in each row of the source array 
    :param miss:    Missing value placeholder 
    :return:        An indexed matrix as a tuple:
    
                    * Dictionary of row key indexes
                    * Dictionary of column key indexes
                    * List of rows, with each row having values. 
    """
    row_keys = { }
    col_keys = { }
    
    for r in array:
        row_key = r[row]
        col_key = r[col]
        row_keys.setdefault( row_key, len( row_keys ) )
        col_keys.setdefault( col_key, len( col_keys ) )
    
    n_rows = len( row_keys )
    n_cols = len( col_keys )
    
    out = [[miss] * n_cols for _ in range( n_rows )]
    
    for r in array:
        row_key = r[row]
        col_key = r[col]
        value = r[val]
        row_i = row_keys[row_key]
        col_i = col_keys[col_key]
        out[row_i][col_i] = value
    
    return row_keys, col_keys, out


def get_permutations( sequence, max_permutations: int, r: Optional[int] = None, rng: Optional[random.Random] = None ):
    """
    Gets permutations from `sequence`.
    
    :param r:                   Length of permutations
    :param sequence:            Sequence
    :param max_permutations:    Maximum number of permutations to return. 
    :return: 
    """
    import itertools
    from math import factorial
    
    if max_permutations <= 0:
        raise ValueError( "max_permutations must be above 0." )
    
    n: int = len( sequence )
    r = r if r is not None else n
    possible_permutations = int( factorial( n ) // factorial( n - r ) )
    
    if max_permutations >= possible_permutations:
        # Use all permutations
        return itertools.permutations( sequence )
    
    # Use a random subset of permutations
    return get_random_permutations( sequence, max_permutations, r, rng = rng )


def get_random_permutations( sequence, max_permutations, r: Optional[int] = None, rng: Optional[random.Random] = None ):
    r = r if r is not None else len( sequence )
    
    if rng is None:
        rng = random.Random()
    
    for n in range( max_permutations ):
        sequence2 = list( sequence )
        rng.shuffle( sequence )
        yield sequence2[:r]


def array_join( array: Iterable[T], delimiter: Iterable[T] = () ) -> List[T]:
    r: List[T] = []
    
    for index, element in enumerate( array ):
        if index != 0:
            r.extend( delimiter )
        
        r.append( element )
    
    return r


class RepeatBlanker( Generic[V] ):
    """
    Replaces repeats in a sequence with a blank value (None).
    """
    __slots__ = "blank", "last"
    __sentinel = object()
    
    
    def __init__( self, blank: V = None ):
        self.blank: V = blank
        self.last = self.__sentinel
    
    
    def __call__( self, value: T, key: U = __sentinel ) -> Union[T, U, V]:
        """
        :param value:   Value to return 
        :param key:     Item to use to test if this is the same as the preceding.
                        If this is not specified the `value` is used. 
        :return:        `value` or the `blank` value. 
        """
        if key is self.__sentinel:
            key = value
        
        if key == self.last:
            return self.blank
        
        self.last = key
        return value
    
    
    def reset( self ):
        self.last = self.__sentinel


def dicts_to_table( dicts: Sequence[Union[Sequence[Tuple[object, object]], Dict[object, object]]],
                    empty: object = None,
                    header: bool = True,
                    headers: Optional[Sequence[object]] = None,
                    col_limit: int = 0
                    ) -> List[List[object]]:
    """
    Converts a sequence of dictionaries into a table, i.e. ::
    
        [
            { "a": 1, "b": 2,        },
            { "a": 3, "b": 4,        },
            { "a": 5,         "c": 6 },
        ]
        
    Becomes::
    
        [
            [ "a", "b", "c" ],
            [  1,   2,   -  ],
            [  3,   4,   -  ],
            [  5,   -,   6  ],
        ]
        
    :param dicts:       Sequence of dictionaries
                        Each "dictionary" may be a `dict` or simply a sequence of key-value pairs. 
    :param empty:       Used for missing values. 
    :param header:      Include the header row in the result. 
    :param headers:     Default headers, can be used to control the header order or insert blank columns.
    :param col_limit:   Limit on number of columns (headers).
                        If this is breached, a `ValueError` is raised.
    :return:            Table, as a list of lists. 
    """
    headers_ = { } if headers is None else create_index_lookup( headers )
    rows = []
    
    for dict_ in dicts:
        if isinstance( dict_, Dict ):
            dict_ = dict_.items()
        
        row = [empty] * len( headers_ )
        
        for key, value in dict_:
            idx = headers_.setdefault( key, len( headers_ ) )
            
            if col_limit and len( headers_ ) > col_limit:
                raise ValueError( "More headers than permitted by column limit." )
            
            ensure_capacity( row, idx, empty )
            
            row[idx] = value
        
        rows.append( row )
    
    if header:
        rows.insert( 0, list( headers_ ) )
    
    return rows
