import filelock


class FileLock:
    class TimeoutError( Exception ):
        pass
    
    
    def __init__( self, file_name, timeout: float = None, period: float = None ):
        self.file_name = file_name
        self.lock = filelock.FileLock( file_name )
        self.timeout = timeout
        self.period = period
    
    
    def acquire( self, timeout: float = None, period: float = None ) -> bool:
        if timeout is None:
            timeout = self.timeout if self.timeout is not None else -1
        
        if period is None:
            period = self.period if self.period is not None else 1
        
        try:
            self.lock.acquire( timeout = timeout,
                               poll_intervall = period )
        except filelock.Timeout:
            return False
        else:
            return True
    
    
    def release( self ):
        self.lock.release()
    
    
    def __enter__( self ):
        if not self.acquire():
            raise TimeoutError( f"Failed to obtain the file lock ({self.file_name}) within the specified timeout ({self.timeout}). If this file should already be unlocked, consider deleting it." )
    
    
    def __exit__( self, exc_type, exc_val, exc_tb ):
        self.release()
