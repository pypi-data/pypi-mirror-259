import multiprocessing
from typing import Callable, Dict, Tuple

from mhelper.exception_recorder import print_traceback, try_get_log_ref


def run_in_separate_process( fun: Callable, *args, **kwargs ):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process( target = _perform,
                                       args = (queue, fun, args, kwargs) )
    process.start()
    process.join()
    result = queue.get()
    
    if isinstance( result, Exception ):
        raise RuntimeError( f"The spawned process raised an error. {try_get_log_ref( result )}." )
    
    return result


def _perform( queue: multiprocessing.Queue,
              fun: Callable,
              args: Tuple,
              kwargs: Dict
              ) -> None:
    try:
        result = fun( *args, **kwargs )
    except Exception as ex:
        print_traceback( ex, ref = True )
        result = ex
    
    queue.put( result )
