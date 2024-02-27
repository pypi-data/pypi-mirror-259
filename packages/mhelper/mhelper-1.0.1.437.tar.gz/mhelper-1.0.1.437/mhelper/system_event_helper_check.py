import os
import sys
import logging


def __main() -> None:
    """
    CLI entry point for this package.
    """
    os.environ["NO_UPDATE_ROIT"] = "1"
    
    from mhelper.system_event_helper import implementation
    
    if "--help" in sys.argv or "-h" in sys.argv:
        print( implementation.__doc__ )
        return
    
    if not implementation._roit_logger.handlers:
        implementation._roit_logger.addHandler( logging.StreamHandler( sys.stdout ) )
    
    if implementation.posix_ipc:
        implementation._unix_update_interests()
    else:
        implementation._roit_log( "There is no ROIT to check - Windows cleans up the threading primitives automatically :)" )


if __name__ == "__main__":
    __main()
