"""
Contains a multithreaded dispatch queue class, for dispatching function calls
into worker threads.

This can be easily converted into a multiprocessed queue, by having the threads
make a system call.
"""
# !EXPORT_TO_README

from threading import Thread
from typing import List, Optional, Union
from mhelper import system_event_helper


class ThreadedDispatcher:
    """
    Asynchronous message queue.
    
    This loops querying a `handler` for tasks. New threads are then spawned to
    perform the tasks.
    
    This queue works across process boundaries, if a new task is available
    then the `ThreadedDispatcher.Notifier` class may be used to inform the
    process running the `ThreadedDispatcher` that it should query the `handler`
    for new tasks. Alternatively, the `ThreadedDispatcher` will periodically
    poll the `handler` for tasks.
    
    All fields should be considered immutable externally.
    
    .. hint::
    
        `Bgts` provides a concrete implementation of this class and is probably
        what you want.  
    
    :ivar handler:              ITaskHandler instance
    :ivar __threads:            List of active threads
    :ivar __thread_index:       Arbitrary incrementer used to name new threads
    :ivar max_num_threads:      Maximum number of active threads
    :ivar poll_frequency:       Timeout on the SYSTEM_EVENT
    :ivar __shutting_down:      When set, indicates the queue is waiting for tasks to finish before it exits its main loop.
    :ivar __shut_down:          When set, indicates that all tasks are finished and the queue is exiting/exited its main loop.
    :ivar __notifier:           A `ThreadedDispatcher.Notifier` instance that is used to construct the system events.
    """
    __slots__ = "__handler", "__thread_index", "threads_lock", "__threads", "__max_num_threads", "__poll_frequency", "__shutting_down", "__shut_down", "__notifier"
    
    
    class InUseError( Exception ):
        pass
    
    
    def __init__( self,
                  handler: "ThreadedDispatcher.IHandler",
                  notifier: Union["ThreadedDispatcher.Notifier", str],
                  max_num_threads: int,
                  poll_frequency: float ):
        super().__init__()
        self.__handler = handler
        self.__threads: List[Thread] = []
        self.__thread_index = 0
        self.__max_num_threads = max_num_threads
        self.__poll_frequency = poll_frequency
        self.__shutting_down = False
        self.__shut_down = False
        self.__notifier = self.Notifier( notifier ) if isinstance( notifier, str ) else notifier
        self.__handler.log( "Threaded task queue created. {} maximum threads, {} second poll interval.", max_num_threads, poll_frequency )
    
    
    class IHandler:
        """
        Designates a class capable of providing tasks for a `ThreadedDispatcher`.
        """
        __slots__ = ()
        
        
        def initialise( self ):
            """
            Called when the dispatcher is about to enter its main loop.
            
            Performs any initialisation that is important to occur only if the
            dispatcher is successfully started.
            """
            pass
        
        
        def acquire_task( self ) -> Optional[object]:
            """
            The implementing class should return an object identifying the task to
            perform, or `None` if no tasks are available. This function is
            guaranteed to always be called from the dispatcher's main thread.
            """
            raise NotImplementedError( "abstract" )
        
        
        def run_task( self, task: object ) -> None:
            """
            The implementing class should run the specified task. This function is
            called from the dispatcher's worker thread.
            
            .. note::
            
                Due to the GIL the `ITaskHandler` itself may wish to spawn a new
                process to run CPU-bound tasks, rather than relying on the worker
                thread to alleviate load.
            """
            raise NotImplementedError( "abstract" )
        
        
        def send_heartbeat( self ) -> bool:
            """
            This is called when the dispatcher is notified or polls. The
            implementing class should perform any periodic actions and return
            whether the dispatcher should continue running. Returning `False` shuts
            down the dispatcher gracefully.
            """
            raise NotImplementedError( "abstract" )
        
        
        def log( self, *args, **kwargs ) -> None:
            """
            Called by the dispatcher to issue logging messages.
            """
    
    
    class Notifier:
        """
        Used by a client to notify a `ThreadedDispatcher` that it should
        acquire tasks and send its heartbeat.
        
        This class is also used by the `ThreadedDispatcher` itself to instantiate
        the system events in the same manner on the server.
        
        :ivar __system_event:       Notifies the dispatcher that new tasks are
                                    available, or that it should send its
                                    heartbeat, rather than waiting for the next
                                    poll.
        :ivar __system_event_pong:    Set by the dispatcher in response to a
                                    `system_event` or poll. Clients may unset
                                    this and wait to check the dispatcher's
                                    status (see `notify`).
        :ivar __system_mutex:       Mutex around the dispatcher's main loop. 
        """
        __slots__ = "__queue_name", "__system_event", "__system_event_pong", "__system_mutex"
        
        
        def __init__( self, queue_name: str ):
            self.__queue_name: str = queue_name
            self.__system_event: Optional[system_event_helper.SystemEvent] = None
            self.__system_event_pong: Optional[system_event_helper.SystemEvent] = None
            self.__system_mutex: Optional[system_event_helper.SystemMutex] = None
        
        
        def __getstate__( self ):
            return { "__queue_name": self.__queue_name }
        
        
        def __setstate__( self, state ):
            self.__queue_name = state["__queue_name"]
            self.__system_event = None
            self.__system_event_pong = None
            self.__system_mutex = None
        
        
        def __initialise( self ):
            if self.__system_event is not None:
                return
            
            self.__system_event = system_event_helper.SystemEvent.create( f"{self.__queue_name}.Ping" )
            self.__system_event_pong = system_event_helper.SystemEvent.create( f"{self.__queue_name}.Pong" )
            self.__system_mutex = system_event_helper.SystemMutex.create( f"{self.__queue_name}.Mutex" )
        
        
        def notify( self, wait: float = None ) -> bool:
            """
            Sets the `system_event`, telling the (remote) `ThreadedDispatcher`
            to try and dispatch tasks.
            
            If `wait` is set, then the function waits for a maximum of `wait`
            seconds and returns whether the dispatcher acknowledged the
            `system_event` via its `system_event_pong` during this time. If wait
            is not set, then this function always returns `False`.
            """
            self.__initialise()
            self.__system_event_pong.clear()
            self.__system_event.set()
            
            if wait is not None:
                return self.__system_event_pong.wait( wait )
            else:
                return False
        
        
        def query_mutex( self, wait: float = 1 ) -> bool:
            """
            Returns if the server is running.
            
            Technically this returns `true` if the mutex is unavailable.
            This won't correlate with the server's state if someone else is
            querying the mutex at the same time or if the server is running but
            has yet to acquire the mutex. `notify` can also be used to check
            the server's status via a different route.
            """
            self.__initialise()
            if self.__system_mutex.acquire( wait ):
                self.__system_mutex.release()
                return False
            
            return True
        
        
        def _poll( self, timeout: float ) -> bool:
            """
            Server side. Internal. Waits on the event.
            """
            self.__initialise()
            is_set = self.__system_event.wait( timeout )
            self.__system_event.clear()
            self.__system_event_pong.set()
            return is_set
        
        
        def _acquire_mutex( self ):
            """
            Server side. Acquires the mutex or raises an exception.
            Remember to `_release_mutex` at some point.
            
            :exception ThreadedDispatcher.InUseError:
            """
            self.__initialise()
            if not self.__system_mutex.acquire( 1 ):
                raise ThreadedDispatcher.InUseError(
                        "The system mutex could not be acquired. "
                        f"This is probably because the {ThreadedDispatcher.__name__}({self.__queue_name!r}) is already running. "
                        f"The mutex in question is {self.__system_mutex}. See also {system_event_helper.__file__}." )
        
        
        def _release_mutex( self ):
            """
            Server side. Releases the mutex.
            """
            self.__system_mutex.release()
    
    
    def __repr__( self ):
        return f"{type( self ).__name__}({self.__notifier!r})"
    
    
    def run_dispatcher_async( self ) -> None:
        """
        Runs the dispatcher in a background process.
        
        :exception InUseError: 
        """
        import multiprocessing
        
        # The mutex is acquired *before* starting the process, which allows us
        # to raise the exception now.
        self.__notifier._acquire_mutex()  # ~~> InUseError
        
        try:
            process = multiprocessing.Process( target = self.run_dispatcher )
            process.start()
        finally:
            # Release the mutex
            # The spawned process should pick it up and enter its main block
            # (It's possible it doesn't, let's say because something else is
            #  hogging the mutex. This would be weird though, and hard to
            #  distinguish from another error, so in the next step we raise a
            #  `RuntimeError` and not an `InUseError`.)
            self.__release_mutex()
        
        if not self.__notifier.notify( 20 ):
            raise RuntimeError( f"The {self} hasn't responded to the query request. "
                                "Please check the logs for errors from the dispatcher itself." )
    
    
    def run_dispatcher( self ) -> None:
        """
        Runs the main dispatcher loop.
        
        This repeatedly calls `__dispatch` until there is nothing more to
        dispatch (because there are no more jobs or no more available threads),
        and then waits on either the poll-time to expire or the SYSTEM_EVENT 
        to be flagged. Then it starts dispatching again.
        
        :exception ThreadedDispatcher.InUseError:
        """
        # See if we are already running
        self.__notifier._acquire_mutex()
        
        try:
            self.__handler.initialise()
            
            self.__dispatch_all( "created" )
            
            while not self.__shut_down:
                is_set = self.__notifier._poll( self.__poll_frequency )
                
                # Send our heartbeat to anyone who cares
                if not self.__handler.send_heartbeat():
                    self.__handler.log( "I have received the shutdown signal from the heartbeat function." )
                    self.__shutting_down = True
                
                self.__dispatch_all( "released" if is_set else "polling" )
        except KeyboardInterrupt:
            pass
        finally:
            self.__release_mutex()
    
    
    def __release_mutex( self ):
        """
        Releases the mutex.
        """
        self.__notifier._release_mutex()
    
    
    def __dispatch_all( self, debug_message: str ) -> None:
        """
        This repeatedly calls `__dispatch` until there is nothing more to
        dispatch (because there are no more jobs or no more available threads).
        """
        while self.__dispatch( debug_message ):
            debug_message = "iterating"
            pass
    
    
    def __dispatch( self, debug_message ) -> bool:
        """
        Obtains a task from the queue and spawns a thread to process it.
        
        Returns `False` if there are no more jobs or no more threads, this
        stops the master until a thread ends or a `SYSTEM_EVENT` is received. 
        """
        # Drop any dead threads
        for thread in list( self.__threads ):
            if not thread.is_alive():
                # BEGIN IMPORTANT
                #   KNOWN BUG
                #   If the thread has died in an unnatural way, the caller will never get their result
                # END
                self.__handler.log( "THREAD #{} WITH TASK #{} HAS ENDED.", *getattr( thread, "TAG_x_args" ) )
                self.__threads.remove( thread )
        
        # Check we aren't at capacity
        num_threads = len( self.__threads )
        
        # If we are shutting down then don't spawn any more tasks...
        if self.__shutting_down:
            self.__handler.log( "WAITING FOR {} THREADS TO END BEFORE SHUT DOWN.", num_threads )
            
            # ...and if there are no more threads then exit
            if num_threads == 0:
                self.__shut_down = True
            
            return False
        
        if num_threads >= self.__max_num_threads:
            self.__handler.log( "Dispatcher {} - at capacity.", debug_message )
            return False
        
        # Get a task
        task_id = self.__handler.acquire_task()
        
        if task_id is None:
            self.__handler.log( "Dispatcher {} - no task.", debug_message )
            return False
        
        if debug_message == "polling":
            # Possible causes:
            # 1. Timing. The dispatcher was notified, but timed-out at the same time as it was
            #    notified. This is more likely if the poll interval is low.
            # 2. Notification. The dispatcher wasn't notified of the new task / free thread.
            # 3. Event. The dispatcher was notified, but something went wrong with the SystemEvent
            #    that should have passed that notification between processes.
            self.__handler.log( "WARNING: Dispatcher had to poll to receive the task. See comments in code.", UserWarning )
        
        # Create a thread for it
        self.__thread_index += 1
        self.__handler.log( "Dispatcher[{}] {} - dispatching task #{} to thread #{}.".format( num_threads, debug_message, task_id, self.__thread_index ) )
        thread = Thread( target = self.__thread_fn,
                         args = (self.__thread_index, task_id),
                         name = "mq_thread_{}".format( self.__thread_index ) )
        setattr( thread, "TAG_x_args", (self.__thread_index, task_id) )
        self.__threads.append( thread )
        thread.start()
        return True
    
    
    def __thread_fn( self, thread_id: int, task_id: int ) -> None:
        try:
            # Execute the task
            self.__handler.log( "Task #{} has been received on thread #{}.".format( task_id, thread_id ) )
            self.__handler.run_task( task_id )
            
            # Notify the dispatcher that they may start another thread
            # (Use the same process clients use to notify us)
            self.__notifier.notify()
        except Exception as ex:
            import mhelper.exception_formatter
            msg = mhelper.exception_formatter.format_traceback( ex,
                                                                message = "An unhandled error has occurred on the worker thread. The dispatcher will now try to exit." )
            self.__handler.log( msg )
            self.__shutting_down = True
