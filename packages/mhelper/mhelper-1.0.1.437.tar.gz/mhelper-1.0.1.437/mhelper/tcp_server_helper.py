"""
TCP Server Helper
=================

* `SocketServer`
    - Boilerplate code for a TCP *server* that runs one thread per client.
* `SocketClient`
    - An accompanying class is provided that provides the boilerplate code for a
      *client* using a similar API to `SocketServer`.
* `SocketHandler`
    - Derive from this to specify the action taken when data is received from
      the server or client.
* `BstrSocketHandler` 
    - A `SocketHandler` allowing a server and client to send and receive *length
      prefixed* messages, a common solution to avoid messages being split.

No magic. No duck typing. Encapsulation over inheritance. WYSIWYG. Annotated. Documented. Tested. 

Usage
-----

::

    from mhelper.tcp_server_helper import SocketServer, SocketClient, BstrSocketHandler 

    class MyHandler( BstrSocketHandler ):
        def on_message_received( self, message ):
            print( "Received {message}" ) 
    
    if "--server" in sys.argv:
        server = SocketServer( handler = MyHandler() )
        server.run()
    else:
        client = SocketClient( handler = MyHandler() )
        client.run_async()
        client.send( "Hello, world!" )
        client.close()


Testing
-------

The package may be run as an executable, which exposes a simple messaging
server and clients for test purposes. 


Requirements
------------

This package is stand alone and has no additional requirements.



:data _BUFFER_SIZE:     *Default* size of the receiver buffers.
:data _DAEMON_THREADS:  Whether we use daemon threads.
                        Turned off during testing because ideally we need to
                        make sure the server cleans up after itself.
                        Turned on for production, we don't want to freeze the
                        user's application if they don't close the server
                        and the server doesn't *need* to clean up.
                        
    
"""
import socket
import threading
from typing import List, Optional
import io


_BUFFER_SIZE: int = 1024
_DAEMON_THREADS: bool = True


class Remote:
    """
    Wraps the remote socket, allowing the `SocketHandler` to optionally
    transform any messages to be sent.
    """
    
    
    def __init__( self, index: int, socket: socket.socket, handler: "SocketHandler" ):
        """
        :param index:       A name unique to the socket's owner.
                            Intended primarily for debugging.
        :param socket:      The actual socket. 
        :param handler:     The handler used to transform the messages. 
        """
        self.index = index
        self.socket = socket
        self.handler = handler
    
    
    def send( self, message: bytes ):
        """
        Sends a message to the remote, applying any transformations denoted by
        the `handler`. Use `socket.send` to send raw bytes directly.
        """
        self.socket.send( self.handler.on_send( message ) )
    
    
    def __repr__( self ):
        return f"{type( self ).__name__}({self.index})"


class Message:
    """
    Wraps the arguments passed to receiver methods.
    """
    __slots__ = "remote", "data"
    
    
    def __init__( self, remote: Remote, data: bytes ):
        """
        :param remote:      Remote connection wrapper 
        :param data:        Data received 
        """
        self.remote = remote
        self.data = data
    
    
    def __repr__( self ):
        return f"{type( self ).__name__}({self.remote!r}, {self.data!r})"


class SocketHandler:
    """
    Designates how to handle receiving messages from the server or client.
    
    The flow is::
    
        on_started        Once
        on_connected      Once per remote
        on_disconnected   Once per remote
        on_received       Once per message
        on_stopped        Once
        
    For the server, there will be zero or more remotes (the clients).
    On the client, there will be one (the server, if successful) or zero
    (nothing, if unsuccessful) remotes.
    
    If a the client fails to connect to the server, the server fails to start
    listening, or no clients ever connect to the server, then `on_stopped` will
    directly follow `on_started`.
    
    Note that Windows will likely kill the server immediately if the port is in
    use, meaning `on_stopped` occurs soon after `on_started`.
    Linux meanwhile will pretend the server is running, although no client will
    ever connect, instead being directed to the existing owner of the port.
    See `socket.create_server` for details.
    
    All arguments are passed by position.
    
    !VIRTUAL
    """
    
    
    def on_started( self ):
        """
        The server has started its main loop.
        The client has started its main loop.
        
        No connection has yet been established.
        
        !VIRTUAL
        """
        pass
    
    
    def on_stopped( self ):
        """
        The server has stopped its main loop.
        The client has stopped its main loop.
        
        !VIRTUAL
        """
        pass
    
    
    def on_connected( self, remote: Remote ) -> None:
        """
        A client has connected to the server.
        The client has connected to the server.
        
        If the client has failed to connect to the server this will not be
        called and `on_stopped` will follow `on_started`.
        
        !VIRTUAL
        """
        pass
    
    
    def on_disconnected( self, remote: Remote ) -> None:
        """
        A client has disconnected from the server.
        The client has disconnected from the server.
        
        !VIRTUAL
        """
        pass
    
    
    def on_bytes_received( self, message: Message ) -> None:
        """
        A message from a client has been received.
        A message from the server has been received.
        
        Note the message may be split into multiple calls if it exceeds the
        buffer size. Use `BstrSocketHandler` if this is an issue.
        
        !VIRTUAL 
        """
        pass
    
    
    def on_send( self, message: bytes ) -> bytes:
        """
        Server about to send a message to client(s).
        Client about to send a message to server.
        
        !VIRTUAL
        
        :param message: Intended message to send 
        :return:        Actual message to send 
        """
        return message


class BstrSocketHandler( SocketHandler ):
    """
    Derivation of `SocketHandler` that length-prefixes messages in order that
    the message is received in whole.
    A new method, `on_received_message` is exposed by which the complete
    message may be captured.
    
    Note this class assumes prefixes on both *outgoing* and *incoming* messages.
    
    Prefixes are 8 byte unsigned little endian integers (UINT32). 
    """
    
    
    def on_send( self, message: bytes ) -> bytes:
        """
        !VIRTUAL !OVERRIDE
        """
        # Add the length prefix to the sent bytes
        pfx = len( message ).to_bytes( 8, "little", signed = False )
        return b"".join( (pfx, message) )
    
    
    def on_bytes_received( self, message: Message ) -> None:
        """
        !VIRTUAL !OVERRIDE
        """
        # Copy the received bytes into our own buffer until the full message is
        # received
        client = message.remote
        
        if not hasattr( client, "BSH_buf" ):
            client.BSH_awaiting = 0
            client.BSH_buf = []
        
        inf = io.BytesIO( message.data )
        
        while inf.tell() != len( message.data ):
            if not client.BSH_awaiting:
                pfx = inf.read( 8 )
                client.BSH_awaiting = int.from_bytes( pfx, "little", signed = False )
            
            nxt = inf.read( client.BSH_awaiting )
            client.BSH_awaiting -= len( nxt )
            client.BSH_buf.append( nxt )
            
            if not client.BSH_awaiting:
                self.on_message_received( Message( client, b"".join( client.BSH_buf ) ) )
                client.BSH_buf.clear()
    
    
    def on_message_received( self, message: Message ) -> None:
        """
        A complete message from a client has been received.
        A complete message from the server has been received.
        
        Unlike `on_bytes_received`, this is the entire message.
        
        !VIRTUAL
        """
        pass


class SocketServer:
    """
    TCP server that runs one thread per client.
    """
    
    
    def __init__( self, host: str, port: int, handler: SocketHandler, *, buffer_size: int = _BUFFER_SIZE ) -> None:
        """
        Constructor.
        :param host:          Host
        :param port:          Port
        :param handler:       A custom SocketServerHandler denoting what to do when
                              messages are received.
        :param buffer_size:   Size of receiver buffers. One per client.
        """
        self.socket: Optional[socket.socket] = None
        self.host: str = host
        self.port: int = port
        self.clients: List[Remote] = []
        self.__main_thread_o: Optional[threading.Thread] = None
        self.handler: SocketHandler = handler
        self.__is_shutdown: bool = False
        self.__client_threads: List[threading.Thread] = []
        self.__num_accepted: int = 0
        self.buffer_size: int = buffer_size
    
    
    def run_async( self ) -> threading.Thread:
        """
        Runs the main loop asynchronously.
        The thread is returned. 
        """
        self.__main_thread_o = threading.Thread( target = self.__main_thread,
                                                 daemon = _DAEMON_THREADS,
                                                 name = "SocketServer Main Thread" )
        self.__main_thread_o.start()
        return self.__main_thread_o
    
    
    def run( self ) -> None:
        """
        Runs the main loop synchronously. 
        """
        # Without polling we can't SIGINT out of the program, so our sync
        # run is actually an async run with a polling wait.  
        thread: threading.Thread = self.run_async()
        
        try:
            while thread.is_alive():
                thread.join( 1 )
        finally:  # e.g. KeyboardInterrupt
            self.close()
    
    
    def close( self ) -> None:
        """
        Stops the server.
        """
        if self.__is_shutdown:
            return
        
        self.__is_shutdown = True
        
        for client in tuple( self.clients ):
            client.socket.close()
        
        if self.socket is not None:
            self.socket.close()
        
        self.handler.on_stopped()
        
        self._assert_ended()
    
    
    def send( self, message: bytes ) -> None:
        """
        Sends a message to *all* clients.
        The `handler` may translate the data into a different format if needed.
        """
        message = self.handler.on_send( message )
        
        for client in self.clients:
            client.socket.send( message )
    
    
    def __main_thread( self ):
        """
        Internal.
        Runs the main loop synchronously.
        Do not call manually, this requires a wrapper in order to be able to
        send SIGINT! 
        """
        self.handler.on_started()
        
        try:
            self.socket = socket.create_server( (self.host, self.port) )
        except Exception:  # OsError, Windows
            self.close()
            return
        
        try:
            while True:
                try:
                    client_socket, address = self.socket.accept()
                except Exception:
                    break
                
                self.__num_accepted += 1
                proxy = Remote( self.__num_accepted, client_socket, self.handler )
                self.clients.append( proxy )
                self.handler.on_connected( proxy )
                thread = threading.Thread( target = self.__client_thread,
                                           args = (proxy,),
                                           daemon = _DAEMON_THREADS,
                                           name = f"SocketServer Client Thread {proxy}" )
                thread.start()
                self.__client_threads.append( thread )
        finally:
            # Not thread safe but this is only in case of error
            self.close()
    
    
    def __client_thread( self, client: Remote ) -> None:
        """
        Internal.
        Runs the main client receiver loop.
        """
        client_socket = client.socket
        
        while True:
            try:
                data: bytes = client_socket.recv( self.buffer_size )
            except Exception:
                break
            
            if not data:
                break
            
            self.handler.on_bytes_received( Message( client, data ) )
        
        client_socket.close()
        self.clients.remove( client )
        self.__client_threads.remove( threading.current_thread() )
        self.handler.on_disconnected( client )
    
    
    def _assert_ended( self ):
        """
        Checks all threads have finished properly.
        
        We cannot check our own thread so if this is called from the server's
        own thread, or any client thread, that particular thread won't be
        checked.
        
        :exception RuntimeError: Threads still running.
        """
        _assert_ended( self.__main_thread_o )
        
        for c_thread in self.__client_threads:
            _assert_ended( c_thread )


class SocketClient:
    """
    TCP client with similar usage to `SocketServer`.
    """
    
    
    def __init__( self, host: str, port: int, handler: SocketHandler, *, timeout: Optional[float] = None, buffer_size: int = _BUFFER_SIZE ):
        """
        Constructor.
        
        :param host:        Host
        :param port:        Port
        :param handler:     A custom `SocketHandler` denoting what to do when
                            messages are received.
        :param timeout:     Timeout on operations. `None` uses the default.
        :param buffer_size: Size of receiver buffer.
        """
        self.__is_shutdown: bool = False
        self.__receiver_thread_o: Optional[threading.Thread] = None
        self.handler: SocketHandler = handler
        self.host: str = host
        self.port: int = port
        self.socket: Optional[socket.socket] = None
        self.timeout: float = timeout
        self.buffer_size: int = buffer_size
    
    
    def run_async( self ) -> threading.Thread:
        """
        Runs the main loop asynchronously.
        The thread is returned. 
        """
        self.__receiver_thread_o = threading.Thread( target = self.__receiver_thread,
                                                     daemon = _DAEMON_THREADS,
                                                     name = "SocketClient Receiver Thread" )
        self.__receiver_thread_o.start()
        return self.__receiver_thread_o
    
    
    def run( self ) -> None:
        """
        Runs the main loop synchronously. 
        """
        # Without polling we can't SIGINT out of the program, so our sync
        # run is actually an async run with a polling wait.
        # TODO: This applies to the SERVER, I'm *assuming* it applies to the
        # client but haven't actually tested it.
        thread: threading.Thread = self.run_async()
        
        try:
            while thread.is_alive():
                thread.join( 1 )
        finally:  # e.g. KeyboardInterrupt
            self.close()
    
    
    def send( self, message: bytes ) -> None:
        """
        Sends a message to the server.
        The `handler` may translate the data into a different format if needed.
        """
        self.socket.send( self.handler.on_send( message ) )
    
    
    def __receiver_thread( self ) -> None:
        """
        Internal.
        Runs the main client receiver loop.
        """
        self.handler.on_started()
        
        self.socket = socket.socket()
        proxy = Remote( 0, self.socket, self.handler )
        
        if self.timeout is not None:
            self.socket.settimeout( self.timeout )
        
        try:
            self.socket.connect( (self.host, self.port) )
        except Exception:  # ConnectionRefusedError
            self.close()
            return
        
        self.handler.on_connected( proxy )
        
        while True:
            try:
                data: bytes = self.socket.recv( self.buffer_size )
            except Exception:
                break
            
            if not data:
                break
            
            self.handler.on_bytes_received( Message( proxy, data ) )
        
        self.handler.on_disconnected( proxy )
        self.close()
    
    
    def close( self ) -> None:
        """
        Stops the client.
        """
        if self.__is_shutdown:
            return
        
        self.__is_shutdown = True
        self.socket.close()
        
        self._assert_ended()
        self.handler.on_stopped()
    
    
    def _assert_ended( self ) -> None:
        """
        Checks all threads have finished properly.
        
        We cannot check our own thread so if this is called from the receiver
        thread, nothing will be checked.
        
        :exception RuntimeError: The thread is still running.
        """
        _assert_ended( self.__receiver_thread_o )


def _assert_ended( thread: threading.Thread ) -> None:
    """
    Checks that a thread has ended.
    
    We cannot check the current thread so if this is called on the current
    thread, no action is performed and nothing will be checked.
    """
    if thread is threading.current_thread():
        return
    
    thread.join( 3 )
    
    if thread.is_alive():
        raise RuntimeError( "The thread failed to terminate within the allotted timeout." )


# noinspection SpellCheckingInspection
def __main():
    """
    Test application entry point.
    
    Usage::
    
        python tcp_server_helper.py --server
        python tcp_server_helper.py --client 
    """
    
    
    class TestSocketHandler( BstrSocketHandler ):
        def on_started( self ):
            print( "on_started" )
        
        
        def on_stopped( self ):
            print( "on_stopped" )
        
        
        def on_connected( self, remote: Remote ) -> None:
            print( f"on_connected        {remote!s:<12}" )
        
        
        def on_disconnected( self, remote: Remote ) -> None:
            print( f"on_disconnected     {remote!s:<12}" )
        
        
        def on_bytes_received( self, message: Message ) -> None:
            print( f"on_bytes_received   {message.remote!s:<12} {message.data}" )
            super().on_bytes_received( message )
        
        
        def on_send( self, message: bytes ) -> bytes:
            print( f"on_send             {' ':<12} {message}" )
            return super().on_send( message )
        
        
        def on_message_received( self, message: Message ) -> None:
            print( f"on_message_received {message.remote!s:<12} {message.data}" )
    
    
    class TestSocketServerHandler( TestSocketHandler ):
        
        # noinspection SpellCheckingInspection
        def on_message_received( self, message: Message ) -> None:
            super().on_message_received( message )
            
            cmd, _, param = message.data.partition( b" " )
            
            if cmd == b"msg":
                print( "SENDING MESSAGE BACK TO CLIENT" )
                message.remote.send( param or b"This is a message" )
            elif cmd == b"msgall":
                print( "SENDING MESSAGE TO ALL CLIENTS" )
                SERVER.send( param or b"This is a message sent to all clients" )
            elif cmd == b"kick":
                print( "KICKING CLIENT" )
                message.remote.socket.close()
            elif cmd == b"kickall":
                print( "KICKING ALL CLIENTS" )
                [client.socket.close() for client in SERVER.clients]
            elif cmd == b"kill":
                print( "CLOSING SERVER UNGRACEFULLY" )
                import os
                os.kill( os.getpid(), 9 )
            elif cmd == b"close":
                print( "CLOSING SERVER GRACEFULLY" )
                SERVER.close()
                SERVER._assert_ended()
    
    
    import sys
    
    
    host: str = "127.0.0.1"
    port: int = 12345
    
    if "--client" in sys.argv:
        print( "***** CLIENT *****" )
        print( """* something        - sent to server
* msg              - server message this client
* msgall           - server message all clients
* kick             - server kick this client
* kickall          - server kick all clients
* kill             - server ungraceful exit
* close            - server graceful exit
* /something       - local command
* /drop            - client ungraceful drop connection
* /kill            - client ungraceful exit
* /close or CTRL+C - client graceful exit
""" )
        
        CLIENT = SocketClient( host, port, TestSocketHandler() )
        main_thread: threading.Thread = CLIENT.run_async()
        from time import sleep
        
        while True:
            try:
                sleep( 0.1 )
                usr_input: str = input( "::" )
            except KeyboardInterrupt:
                print( "CLOSING CLIENT GRACEFULLY" )
                CLIENT.close()
                break
            
            if not main_thread.is_alive():
                print( "CLIENT IS NO LONGER RUNNING, EXITING." )
                CLIENT.close()
                break
            
            if usr_input.startswith( "/" ):
                usr_input = usr_input[1:]
                
                if usr_input == "drop":
                    print( "DISCONNECTING OWN SOCKET" )
                    CLIENT.socket.close()
                    continue
                elif usr_input == "exit":
                    print( "CLOSING CLIENT UNGRACEFULLY" )
                    exit( 0 )
                    break
                elif usr_input == "close":
                    print( "CLOSING CLIENT GRACEFULLY" )
                    CLIENT.close()
                    break
                
                return
            
            usr_message: bytes = usr_input.encode( "utf8" )
            
            try:
                CLIENT.send( usr_message )
            except Exception as ex:
                print( f"COULD NOT SEND ({ex.__class__.__name__}), EXITING" )
                CLIENT.close()
                break
    elif "--server" in sys.argv:
        print( "***** SERVER *****" )
        print( "* CTRL+C - server graceful exit" )
        SERVER = SocketServer( host, port, TestSocketServerHandler() )
        
        try:
            SERVER.run()
        except KeyboardInterrupt:
            SERVER.close()
    else:
        print( "[--client] | [--server]" )


if __name__ == "__main__":
    __main()
