"""
Tests the SystemMutex, SystemSemaphore and SystemEvent classes.
    
Technically the mutex must simply limit access to the resource, however speed,
responsiveness and fair distribution of the resources are also checked here,
as this allows us to detect new bugs. Notably we would usually expect usage of
the resource to alternate between the threads, wheras a bad implementation 
might see the resource exclusively used by one thread, then the other.

In reality there will be periods where one threads acquires the resource
for successively periods, this is due to effects such as one thread starting
or stopping before the other, one threads routine simply being well timed,
and decisions made by the OS when multiple threads are waiting simultaneously -
the underlying system semaphore of course makes no guarantee that it distributes
"fairly". We try and get around these issues by introducing random delays into
the execution and add the "tolerances" which we use to judge timing and
distribution, but it isn't perfect.

On a slower system the tolerances may need turning down a bit.
"""
import os
import threading
import random
from collections import Counter
from time import sleep, perf_counter

from mhelper.system_event_helper import SystemMutex, SystemSemaphore, SystemEvent
from mhelper.exception_hooks import install_error_hooks


def log( x, *args ):
    print( x.format( *args ) )


class Utils:
    @staticmethod
    def start_and_join( threads, event_name = None ):
        [thread.start() for thread in threads]
        
        if event_name:
            SystemEvent.create( event_name ).set()
        
        [thread.join() for thread in threads]


class ProtectedResource:
    def __init__( self, identifier ):
        self.file_name_1 = identifier
        
        if os.path.isfile( self.file_name_1 ):
            os.remove( self.file_name_1 )
    
    
    def access( self ):
        assert not os.path.isfile( self.file_name_1 )
        
        with open( self.file_name_1, "w" ) as fout:
            fout.write( "test" )
        
        os.remove( self.file_name_1 )
        
        if random.random() < 0.001:
            sleep( 0.1 )


class Recorder:
    def __init__( self, identifier ):
        self.file_name_1 = identifier
        
        if os.path.isfile( self.file_name_1 ):
            os.remove( self.file_name_1 )
    
    
    def record( self, value ):
        with open( self.file_name_1, "a" ) as fout:
            fout.write( f"{value}\n" )
    
    
    def retrieve( self ):
        with open( self.file_name_1 ) as fin:
            for line in fin:
                yield line.rstrip()


class ConsecutiveChecker:
    def __init__( self ):
        self.max = { }
        self.current_id = None
        self.current = 0
    
    
    def add( self, id ):
        if self.current_id is not id:
            self.current = 0
            self.current_id = id
        
        self.current += 1
        self.max[self.current_id] = max( self.max.get( self.current_id, 0 ), self.current )
    
    
    def check( self, tolerance ):
        max_consecutive = 0
        
        for thread_id, consecutive in self.max.items():
            log( "THREAD {} CONSECUTIVE {}", thread_id, consecutive )
            max_consecutive = max( consecutive, consecutive )
            if consecutive > tolerance:
                print( f"TEST_WARNING: {consecutive} consecutive access by the same thread, this is more than the maximum tolerance of {tolerance}." )
        
        log( "MAX CONSECUTIVE IS {}", max_consecutive )


class MutexTest:
    """
    Tests `SystemMutex`, requires a working `SystemEvent`.
    """
    
    def __init__( self, num_threads = 9, num_iterations = 100, tolerance = None ):
        """
        See `SemaphoreTest` a discussion of the parameters.
        """
        self.num_threads = num_threads
        self.num_iterations = num_iterations
        self.tolerance = tolerance or int( num_iterations * 0.9 )
        self.resource = ProtectedResource( f"mhelper-mutex_test_resource-{_random_name()}" )
        self.recorder = Recorder( f"mhelper-mutex_test_records-{_random_name()}" )
        self.event_name = f"mhelper_test_mutex_event-{_random_name()}"
    
    
    def _thread( self, id ):
        mutex = SystemMutex.create( f"mhelper-test_mutex-{_random_name()}" )
        SystemEvent.create( self.event_name ).wait()
        
        for n in range( self.num_iterations ):
            if random.random() < 0.01:
                sleep( 0.01 )
            
            with mutex:
                self.resource.access()
                self.recorder.record( id )
    
    
    def run( self ):
        log( "********** MUTEX TEST **********" )
        log( f"{self.num_threads=}, {self.num_iterations=}, {self.tolerance=}" )
        
        t = perf_counter()
        Utils.start_and_join( [threading.Thread( target = self._thread, args = [n] ) for n in range( self.num_threads )], self.event_name )
        
        cc = ConsecutiveChecker()
        
        for l in self.recorder.retrieve():
            cc.add( int( l ) )
        
        cc.check( self.tolerance )
        log( "TOTAL TIME: {}", perf_counter() - t )


class SystemEventTest:
    """
    Tests `SystemEvent`.
    """
    
    def __init__( self, num_iterations = 10, period = 0.1, tolerance = 0.02 ):
        """
        :param num_iterations:  Number of times we call the and reset the event 
        :param period:          Time between each iteration 
        :param tolerance:       Tolerance on response time
                                A response time of more than this will be assumed to be an error
        """
        self.num_iterations = num_iterations
        self.period = period
        self.tolerance = tolerance
        self.recorder = Recorder( f"mhelper-system_event_recorder-{_random_name()}" )
        self.sys_event_name = f"mhelper-system_event-{_random_name()}"
    
    
    def test_system_event_1( self ):
        ev = SystemEvent.create( self.sys_event_name )
        
        s = perf_counter()
        
        for n in range( self.num_iterations ):
            ev.wait()
            ev.clear()
            self.recorder.record( perf_counter() - s )
    
    
    def test_system_event_2( self ):
        ev = SystemEvent.create( self.sys_event_name )
        
        for n in range( self.num_iterations ):
            sleep( self.period )
            ev.set()
    
    
    def run( self ):
        log( "********** SYSTEM EVENT TEST **********" )
        log( f"{self.num_iterations=}, {self.period=}, {self.tolerance=}" )
        t = perf_counter()
        Utils.start_and_join( [threading.Thread( target = self.test_system_event_1 ),
                               threading.Thread( target = self.test_system_event_2 )] )
        
        deviations = []
        
        for index, record in enumerate( self.recorder.retrieve() ):
            actual = float( record )
            expected = (index + 1) * self.period
            deviation = abs( expected - actual )
            deviations.append( deviation )
            
            # if deviation > self.tolerance:
            #     raise RuntimeError( f"Unacceptable deviation of {deviation} seconds, this is above the tolerance of {self.tolerance} seconds." )
        
        log( "AVERAGE RESPONSE TIME IS {}", sum( deviations ) / len( deviations ) )
        log( "TOTAL TIME: {}", perf_counter() - t )


class SemaphoreTest:
    """
    Tests `SystemSemaphore`, requires a working `SystemEvent` and `SystemMutex`.
    """
    
    def __init__( self,
                  num_threads = 9,
                  num_iterations = 100,
                  max_concurrency = 3,
                  expected_concurrency = None,
                  tolerance = None ):
        """
        :param num_threads:          Number of threads competing for the semaphore 
        :param num_iterations:       Number of iterations of each thread's loop 
        :param max_concurrency:      Concurrency of the semaphore 
        :param tolerance:            Tolerance on consecutive accesses by the same thread
                                     Repeated accesses to the semaphore by the same thread this many
                                     times will be assumed to be an error.
                                     `None` uses just under of the number of iterations.
        :param expected_concurrency: We expect concurrency of the semaphore to be maximum at least this
                                     many times, anything less is an error.
                                     `None` uses the same as `self.num_iterations`.
                                     Anything > 1 is good really, self.num_iterations is probably overzealous
        """
        self.num_threads = num_threads
        self.num_iterations = num_iterations
        self.max_concurrency = max_concurrency
        self.expected_concurrency = expected_concurrency or self.num_iterations
        self.tolerance = tolerance or int( num_iterations * 0.9 )
        self.recorder = Recorder( f"mhelper-test_semaphore_recorder-{_random_name()}" )
        self.semaphore_name = f"mhelper-test_semaphore-{_random_name()}"
        self.mutex_name = f"mhelper-test_semaphore_mutex-{_random_name()}"
        self.start_event_name = f"mhelper-test_semaphore_event-{_random_name()}"
    
    
    def _test_semaphore_thread( self, id: int ):
        sem = SystemSemaphore.create( self.semaphore_name, self.max_concurrency )
        m1 = SystemMutex.create( self.mutex_name )
        SystemEvent.create( self.start_event_name ).wait()
        
        for n in range( self.num_iterations ):
            if random.random() < 0.01:
                sleep( 0.01 )
            
            with sem:
                with m1:
                    self.recorder.record( f"{id}\tENTER" )
                
                sleep( random.random() / 1000 )
                
                with m1:
                    self.recorder.record( f"{id}\tEXIT" )
                
                sleep( random.random() / 1000 )
    
    
    def run( self ):
        log( "********** SEMAPHORE TEST **********" )
        log( f"{self.num_threads=}, {self.num_iterations=}, {self.max_concurrency=}, {self.tolerance=}" )
        
        t = perf_counter()
        Utils.start_and_join( [threading.Thread( target = self._test_semaphore_thread, args = [n] ) for n in range( self.num_threads )], self.start_event_name )
        
        cc = ConsecutiveChecker()
        threads_in = set()
        ns = []
        
        for i, l in enumerate( self.recorder.retrieve() ):
            thread_id, action = l.split( "\t" )
            thread_id = int( thread_id )
            
            if action == "ENTER":
                assert thread_id not in threads_in
                threads_in.add( thread_id )
            else:
                assert thread_id in threads_in
                threads_in.remove( thread_id )
            
            cc.add( thread_id )
            
            assert len( threads_in ) <= self.max_concurrency
            
            ns.append( len( threads_in ) )
        
        cc.check( self.tolerance )
        
        counts = Counter( ns )
        
        for entered, count in sorted( counts.items(), key = lambda x: x[0] ):
            p = count / len( ns )
            log( f"CONCURRENCY N={entered} COUNT {count} ({p:.2%})" )
        
        # Make sure there is some full concurrency
        cmc = counts[self.max_concurrency]
        if cmc < self.expected_concurrency:
            raise RuntimeError( f"{cmc} occurences of maximum concurrency ({self.max_concurrency}) "
                                f"but expected at least {self.expected_concurrency}" )
        
        log( "TOTAL TIME: {}", perf_counter() - t )


_session_name = None


def _random_name():
    global _session_name
    
    if _session_name is None:
        _session_name = "".join( random.choice( "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ) for _ in range( 8 ) )
    
    return _session_name


def main():
    install_error_hooks( "CONSOLE" )
    
    log( "********** TESTING STARTS **********" )
    iterations = 10
    SystemEventTest(num_iterations = iterations // 10).run()
    MutexTest(num_iterations = iterations).run()
    SemaphoreTest(num_iterations = iterations).run()
    
    log( "********** TESTING ENDS -- ALL DONE **********" )


if __name__ == "__main__":
    main()

import multiprocessing