import sys
from mhelper import bg_task_helper as BG, log_helper
import time


config = BG.FileBasedBgtsConfig( "Asynchronous hello, world!" )
app = BG.Bgts( config )


def my_async_task( message ):
    print( f"{message} start." )

    for n in range( 5 ):
        time.sleep( 6 )
        print( f"{message} {5 - n}..." )

    print( f"{message} end." )


def main():
    log_helper.LogServer.start()

    if len( sys.argv ) != 2:
        print( "Bad arguments" )
        return

    message = sys.argv[1]

    if message == "serve":
        app.start_dispatcher()
    elif message == "stop":
        app.stop_dispatcher_no_wait()
    elif message == "query":
        app.query_dispatcher()
    else:
        app.submit_task( my_async_task, [message] )


if __name__ == "__main__":
    main()
