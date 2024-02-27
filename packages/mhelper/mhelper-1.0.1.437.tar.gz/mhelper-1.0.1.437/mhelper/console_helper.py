class _Getch:
    """
    Gets a single character from standard input.
    Does not echo to the screen.
    
    BEGIN ATTRIBUTION
        TITLE how-to-read-a-single-character-from-the-user
        PURPOSE Getch (including the Unix and Windows variants)
        AUTHOR tehvan
        WEBSITE https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
        LICENSE-NAME cc by-sa
        LICENSE-URL https://stackoverflow.com/help/licensing
        date-retrieved 2021-05-25
    END ATTRIBUTION
    """

    def __call__( self ):
        raise NotImplementedError( "abstract" )


class _GetchUnix( _Getch ):
    def __call__( self ):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr( fd )
        try:
            tty.setraw( sys.stdin.fileno() )
            ch = sys.stdin.read( 1 )
        finally:
            termios.tcsetattr( fd, termios.TCSADRAIN, old_settings )
        return ch


class _GetchWindows( _Getch ):

    def __call__( self ):
        import msvcrt
        return msvcrt.getch()


getch: _Getch

try:
    import msvcrt
except ImportError:
    getch = _GetchUnix()
else:
    getch = _GetchWindows()
