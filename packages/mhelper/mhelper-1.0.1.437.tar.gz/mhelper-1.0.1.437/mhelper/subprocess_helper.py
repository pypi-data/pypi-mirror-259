"""
Wraps a subprocess, creating threads to monitor its output, allowing a
process's output to be recorded and displayed in real-time.
"""
# !EXPORT_TO_README
from dataclasses import dataclass
from queue import Empty, Queue
from threading import Event, Thread
from typing import Callable, IO, List, Union, Sequence, Optional

import os
import subprocess
import warnings

from mhelper import ansi, exception_helper, log_helper


log = log_helper.Logger( "mhelper.subprocess_helper.AsyncSubprocess" )

_DOnOutput = Callable[[str], None]


class AsyncSubprocess:
    """
    Runs a process asynchronously.
    
    The virtual methods should be overridden to control behaviour. 
    """
    
    
    def __init__( self,
                  *,
                  command: List[str],
                  directory: str = None,
                  send: Union[str, bool, None] = None ) -> None:
        """
        CONSTRUCTOR
        
        :param command:         Command to execute 
        :param directory:       Directory to execute command within 
        :param send:            Standard input to send
        
                                `None` - Nothing to send, close stdin ASAP
                                `True` - Keep stdin open
                                `str` - Send this to stdin, then close stdin.
        """
        self.command = command
        self.directory = directory
        self.send = send
        
        self.process: Optional[subprocess.Popen] = None
    
    
    def on_thread_stdout( self, line ):
        """
        !VIRTUAL !THREAD_UNSAFE
        
        Called when a line of stdout is received, runs in its own thread.
        
        The base implementation calls `on_output_received`.
        """
        self.on_thread_out( line )
    
    
    def on_thread_stderr( self, line ):
        """
        !VIRTUAL !THREAD_UNSAFE
        
        Called when a line of stderr is received, runs in its own thread.
        
        The base implementation calls `on_output_received`.
        """
        self.on_thread_out( line )
    
    
    def on_thread_out( self, line ):
        """
        !VIRTUAL !THREAD_UNSAFE
        
        Called when a line of stdout or stderr is received, runs in its own thread.
        """
        pass
    
    
    def on_thread_process_exit( self ):
        """
        !VIRTUAL !THREAD_UNSAFE
        
        Called when the process exits, runs in its own thread.
        """
        pass
    
    
    def on_thread_stdout_close( self ):
        pass
    
    
    def on_thread_stderr_close( self ):
        pass
    
    
    def run( self ):
        """
        Starts the subprocess.
        """
        
        if self.directory is not None:
            if not os.path.isdir( self.directory ):
                raise FileNotFoundError( "Not a directory: " + self.directory )
            
            orig_cwd = os.getcwd()
            os.chdir( self.directory )
        else:
            orig_cwd = None
        
        self.process = subprocess.Popen( self.command,
                                         stdout = subprocess.PIPE,
                                         stderr = subprocess.PIPE,
                                         stdin = subprocess.PIPE )
        
        if self.directory is not None:
            os.chdir( orig_cwd )
        
        # Stdin argument?
        if self.send is True:
            pass
        elif self.send is not None:
            self.process.stdin.write( self.send.encode( "UTF-8" ) )
            self.process.stdin.close()
        else:
            self.process.stdin.close()
        
        # Read asynchronously
        thread_1 = Thread( target = self.__stream_watching_thread, args = (self.process.stdout, self.on_thread_stdout, 1) )
        thread_1.name = "async_run.stdout_thread(" + " ".join( self.command ) + ")"
        thread_1.daemon = True
        thread_1.start()
        
        thread_2 = Thread( target = self.__stream_watching_thread, args = (self.process.stderr, self.on_thread_stderr, 2) )
        thread_2.name = "async_run.stderr_thread(" + " ".join( self.command ) + ")"
        thread_2.daemon = True
        thread_2.start()
        
        thread_3 = Thread( target = self.__exit_watching_thread, args = () )
        thread_2.name = "async_run.exit_thread(" + " ".join( self.command ) + ")"
        thread_3.daemon = True
        thread_3.start()
    
    
    def __stream_watching_thread( self, out: IO, call, no: int ) -> None:
        log( "SP watching stream." )
        
        while True:
            line_ = out.readline()
            
            if not line_:
                break
            
            line = line_.decode()
            
            if line.endswith( "\n" ):
                line = line[:-1]
            
            call( line )
        
        out.close()
        
        if no == 1:
            self.on_thread_stdout_close()
        else:
            self.on_thread_stderr_close()
    
    
    def __exit_watching_thread( self ) -> None:
        self.process.wait()
        self.on_thread_process_exit()
    
    
    def raise_any_error( self ):
        """
        A convenience method which, if the process has exited with a non-zero
        return, raises a `SubprocessError`.
        """
        if self.process.returncode:
            raise exception_helper.SubprocessError(
                    "SubprocessError 2. The command «{}» exited with error code «{}». "
                    "If available, checking the output may provide more details."
                        .format( " ".join( '"{}"'.format( x ) for x in self.command ),
                                 self.process.returncode ),
                    return_code = self.process.returncode )


class SafeAsyncSubprocess( AsyncSubprocess ):
    """
    A variation of `AsyncSubprocess` that uses an event and queues to issue
    events on the main thread only.
    
    The virtual methods should be overridden to control behaviour:
    
    * `on_stderr`
    * `on_stdout`
    
    Since callbacks are on the main thread, a call to some function is required:
    
    * `wait`
    * `wait_for_exit`
    * `process_queue`
    """
    
    
    def __init__( self,
                  command: List[str],
                  *,
                  directory: str = None,
                  send: Union[str, bool, None] = None,
                  event: Event = None ):
        """
        :param command:         Inherited
        :param directory:       Inherited
        :param send:            Inherited
        :param event:           The wait `Event` to fire when messages are received or the
                                subprocess exits. If this is `None` a new `Event` is used. 
        """
        super().__init__( command = command,
                          directory = directory,
                          send = send )
        
        self.event = event if event is not None else Event()
        self.queue = Queue()
        self.__process_exited = False
        self.__stdout_exited = False
        self.__stderr_exited = False
        self.__all_done = False
    
    
    def on_thread_stdout( self, line ):
        """
        !FINAL
        
        Derived classes should now override the thread-safe `on_stdout`.
        """
        log( "QUEUE stdout" )
        self.queue.put( (1, line) )
        self.event.set()
    
    
    def on_thread_stderr( self, line ):
        """
        !FINAL
        
        Derived classes should now override the thread-safe `on_stderr`.
        """
        log( "QUEUE stderr" )
        self.queue.put( (2, line) )
        self.event.set()
    
    
    def on_thread_process_exit( self ):
        """
        !FINAL
        
        Derived classes should now override the thread-safe `on_exit`.
        """
        log( "QUEUE process exit" )
        self.queue.put( (3,) )
        self.event.set()
    
    
    def on_thread_stderr_close( self ):
        log( "QUEUE stderr close" )
        self.queue.put( (5,) )
        self.event.set()
    
    
    def on_thread_stdout_close( self ):
        log( "QUEUE stdout close" )
        self.queue.put( (4,) )
        self.event.set()
    
    
    def on_stdout( self, line ):
        """
        !VIRTUAL
        
        Called when a line of stdout is received. Runs in the main thread. 
        """
        pass
    
    
    def on_stderr( self, line ):
        """
        !VIRTUAL
        
        Called when a line of stderr is received. Runs in the main thread.
        """
        pass
    
    
    def on_exit( self ):
        """
        !VIRTUAL
        
        Called when the process exits and all data has been acquired. Runs in the main thread.
        """
    
    
    def process_queue( self ) -> bool:
        """
        Non-blocking. Checks and empties the stdout/stderr queues into their
        respective destinations.
        
        Unlike `wait` the wait `Event` is not required to process the queue, so
        the function exits immediately. This can be called if multiple
        `SafeAsyncSubprocess` share the same event.
        
        :return: True unless the process has exited *and* the streams have closed.
        """
        while True:
            try:
                data = self.queue.get_nowait()
            except Empty:
                log( "Nothing in queue." )
                break
            
            code = data[0]
            
            if code == 1:
                log( "DEQUEUE stdout" )
                self.on_stdout( data[1] )
            elif code == 2:
                log( "DEQUEUE stderr" )
                self.on_stderr( data[1] )
            elif code == 3:
                log( "DEQUEUE process exit" )
                self.__process_exited = True
            elif code == 4:
                log( "DEQUEUE stdout close" )
                self.__stdout_exited = True
            elif code == 5:
                log( "DEQUEUE stderr close" )
                self.__stderr_exited = True
            else:
                assert False
        
        if self.__process_exited and self.__stdout_exited and self.__stderr_exited:
            if not self.__all_done:
                self.__all_done = True
                self.on_exit()
            
            return False
        
        return True
    
    
    def wait( self ) -> bool:
        """
        Wait for event, then process queue.
        
        :return: True unless the process has exited *and* the streams have closed.
        """
        log( "SSP waiting" )
        self.event.wait()
        self.event.clear()
        return self.process_queue()
    
    
    def wait_for_exit( self ):
        """
        Repeatedly calls `wait` until the subprocess exits.
        :return: 
        """
        while self.wait():
            pass
        
        log( "SSP exited" )
        
        assert self.queue.qsize() == 0, "Still data queued!"


@dataclass
class ExecuteResult:
    out: Union[str, List[str], None]
    stdout: Union[str, List[str], None]
    stderr: Union[str, List[str], None]
    code: Union[int, None]


class CollectingSafeAsyncSubprocess( SafeAsyncSubprocess ):
    """
    A concrete implementation of `SafeAsyncSubprocess` that collects the output
    in lists. 
    """
    
    
    def __init__( self,
                  command: List[str],
                  *,
                  directory: str = None,
                  send: Union[str, bool, None] = None,
                  event = None,
    
                  on_stdout: _DOnOutput = None,
                  on_stderr: _DOnOutput = None,
                  echo: bool = False,
                  raise_errors: bool = False,
    
                  rx_stdout: bool = False,
                  rx_stderr: bool = False,
                  rx_out: bool = False ):
        """        
        :param command:         !INHERITED
         
        :param directory:       !INHERITED
        
        :param send:            !INHERITED
        
        :param event:           !INHERITED
        
        :param on_stdout:       Adds a custom callback.
         
        :param on_stderr:       Adds a custom callback.
        
        :param echo:            Includes inbuilt callbacks:
        
                                * on_stdout --> echo
                                * on_stderr --> echo
                                    
                                Also causes `command` to be echoed.
                                 
        :param raise_errors:    Include inbuilt callback:
        
                                * on_exit --> raise error if the exit code is non-zero.
                                 
        :param rx_stdout:       Include inbuilt callback:
                    
                                * on_stdout --> add to `self.stdout` list
                                
                                If `rx_stdout` *is* a list, then it is used as `self.stdout`.
                                
        :param rx_stderr:       Include inbuilt callback:
                    
                                * on_stdout --> add to `self.stderr` list
                                
                                If `rx_stderr` *is* a list, then it is used as `self.stderr`.
                                
        :param rx_out:          Includes inbuilt callbacks:
        
                                * on_stdout --> add to `self.out` list
                                * on_stderr --> add to `self.out` list
                                
                                If `rx_out` *is* a list, then it is used as `self.out`.
        """
        super().__init__( command, directory = directory, send = send, event = event )
        self.raise_errors = raise_errors
        
        # Destinations
        if on_stdout is None:
            on_stdout = self.__ignore
        
        if on_stderr is None:
            on_stderr = self.__ignore
        
        # Echo?
        if echo:
            print( ansi.BACK_BLACK + ansi.FORE_YELLOW + "{}".format( command ) + ansi.RESET )
            on_stdout = self.__PrintStdOut( "O>" + ansi.BACK_BLACK + ansi.FORE_GREEN, on_stdout )
            on_stderr = self.__PrintStdOut( "E>" + ansi.BACK_BLACK + ansi.FORE_RED, on_stderr )
        
        # Buffer into arrays?
        if rx_out is not None and rx_out is not False:
            self.out = [] if rx_out is True else rx_out
            on_stdout = self.__Collect( self.out, on_stdout )
            on_stderr = self.__Collect( self.out, on_stderr )
        else:
            self.out = None
        
        if rx_stdout is not None and rx_stdout is not False:
            self.stdout = [] if rx_stdout is True else rx_stdout
            on_stdout = self.__Collect( self.stdout, on_stdout )
        else:
            self.stdout = None
        
        if rx_stderr is not None and rx_stderr is not False:
            self.stderr = [] if rx_stderr is True else rx_stderr
            on_stderr = self.__Collect( self.stderr, on_stderr )
        else:
            self.stderr = None
        
        self.on_stdout = on_stdout
        self.on_stderr = on_stderr
    
    
    @staticmethod
    def __ignore( _ ):
        pass
    
    
    def on_exit( self ):
        if self.raise_errors:
            self.raise_any_error()
    
    
    class __PrintStdOut:
        def __init__( self, pfx, chained ):
            self.pfx = pfx
            self.chained = chained
        
        
        def __call__( self, line ):
            print( self.pfx + line + ansi.RESET )
            self.chained( line )
    
    
    class __Collect:
        def __init__( self, array: List[str], chained ):
            self.array = array
            self.chained = chained
        
        
        def __call__( self, line ):
            self.array.append( line )
            self.chained( line )


def execute( command: List[str],
             *,
             dir: str = None,
             on_stdout: _DOnOutput = None,
             on_stderr: _DOnOutput = None,
             echo: bool = False,
             err: bool = False,
             tx: Union[str, bool, None] = None,
             keep_lines: bool = False,
             rx_stdout: bool = False,
             rx_stderr: bool = False,
             rx_out: bool = False,
             rx_code: bool = False ) -> Union[str, int, list, ExecuteResult]:
    """
    Executes an external command.
    
    This function uses `SafeAsyncSubprocess`.
    
    * Blocks until it completes,
    * The command is executed in its own thread.
    
    Parameters marked † are documented in `CollectingSafeAsyncSubprocess.__init__`.
    
    :param command:             †  
    :param dir:                 * `str` --> Working directory.
                                            The original is restored after execution.
                                * `None` --> Do not change
    :param on_stdout:           † 
    :param on_stderr:           †
    :param echo:                † 
    :param err:                 † (as `raise_errors`)
    :param tx:                  † 
    :param rx_stdout:           †
    :param rx_stderr:           † 
    :param rx_out:              †
    :param keep_lines:          When `True`, buffers are returned as lists.
    :param rx_code:             When `True`, the exit code is returned.
                                This is implicit if no other `rx_` arguments are passed.
                                
    :return: Either the single value requested, or an `ExecuteResult` object if
             multiple `rx_` results were requested.
    """
    # Stream arguments?    
    ex = CollectingSafeAsyncSubprocess( command = command,
                                        on_stdout = on_stdout,
                                        on_stderr = on_stderr,
                                        directory = dir,
                                        send = tx,
                                        echo = echo,
                                        rx_out = rx_out,
                                        rx_stderr = rx_stderr,
                                        rx_stdout = rx_stdout,
                                        raise_errors = err )
    
    ex.run()
    ex.wait_for_exit()
    
    xr = ExecuteResult( __as( keep_lines, ex.out ) if rx_out else None,
                        __as( keep_lines, ex.stdout ) if rx_stdout else None,
                        __as( keep_lines, ex.stderr ) if rx_stderr else None,
                        ex.process.returncode if rx_code else None )
    
    if sum( (rx_out, rx_stdout, rx_stderr, rx_code) ) == 1:
        return (xr.out if rx_out else
                xr.stdout if rx_stdout else
                xr.stderr if rx_stderr else
                xr.code if rx_code else
                "?")
    
    return xr


def __as( keep_lines, array ):
    if keep_lines:
        return array
    else:
        return "\n".join( array )


# region Deprecated
def run( wd: str, cmd: Union[str, Sequence[str]], *, echo = False ):
    warnings.warn( "Deprecated - use execute", DeprecationWarning )
    if isinstance( cmd, str ):
        cmd = cmd.split( " " )
    return execute( dir = wd,
                    command = cmd,
                    echo = echo,
                    rx_stdout = True )


def run_subprocess( wd: str, cmd: Union[str, Sequence[str]], *, echo = False ) -> str:
    warnings.warn( "Deprecated - use execute", DeprecationWarning )
    if isinstance( cmd, str ):
        cmd = cmd.split( " " )
    return execute( dir = wd,
                    command = cmd,
                    echo = echo,
                    rx_stdout = True )
# endregion
