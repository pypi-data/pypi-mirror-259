"""
This package wraps and fixes issues with the `keyring` library on Ubuntu (see
the `get_keyring` function for more details).

It also contains a `ManagedPassword` class, which allows passwords to be pickled
and unpickled whilst keeping the actual password data only on the keyring.

The package can be also used as an executable, allowing keyring passwords to
be read and written via the command line

* Read a password::

    python -m mhelper.password_helper --get <service_name> <user_name>
    
* Write a password::

    python -m mhelper.password_helper --set <service_name> <user_name> <password>

* Write a password, use secure prompt::

    python -m mhelper.password_helper --set <service_name> <user_name>
    
* Remove a password::

    python -m mhelper.password_helper --del <service_name> <user_name>
    
* Test the keyring and this package::

    python -m mhelper.password_helper --test
"""
# !EXPORT_TO_README
from typing import Dict, Optional

__K_ENV_VAR_CHECK = "MJR_KEYRING_CHECK"
__K_ENV_VAR_CRYPTFILE = "KEYRING_CRYPTFILE_PASSWORD"
__g_keyring = None


class ProblematicKeyringError( RuntimeError ):
    pass


def get_keyring():
    """
    Python's `keyring` module is problematic (notably on Ubuntu).
     
    Problem 1 is that the module  back to an error-producing backend if we
    couldn't start a normal backend. Not only does this hide the reason the
    normal backend didn't start, but confusingly tells us we have no backends
    available.
    
    Problem 2 is that if using a GUIless connection, such as SSH on Ubuntu, then
    the module attempts to make a DBus connection that never connects and
    with an infinite timeout, thus freezing the process.
    
    This function:
        * sets up the usual backend on Ubuntu *before* we import `keyring`.
        * translates the errors, producing only `RuntimeError` on failure.
        * tests that passwords can actually be retrieved
        * tests that the module isn't freezing
        
    The `keyring` package is returned on success.
    """
    global __g_keyring

    if __g_keyring is not None:
        return __g_keyring

    __check_for_freezing()

    __g_keyring = __get_keyring()
    return __g_keyring


def __check_for_freezing():
    #
    # Problem 2: Check for freezing
    #
    import subprocess
    import sys
    import os

    timeout_str = os.getenv( __K_ENV_VAR_CHECK, "30" )

    try:
        timeout = int( timeout_str )  # We need to give enough time for the user to accept
    except:
        raise RuntimeError( f"Cannot parse timeout value: {__K_ENV_VAR_CHECK}={timeout_str!r}" )

    if timeout < 0:
        raise RuntimeError( f"Out of bounds timeout value: {__K_ENV_VAR_CHECK}={timeout}" )
    elif timeout == 0:
        return

    process = subprocess.Popen( [sys.executable, __file__, "--check"] )
    is_freezing = False

    try:
        process.wait( timeout )
    except subprocess.TimeoutExpired:
        is_freezing = True
        process.terminate()
        process.wait()

    if is_freezing:
        raise ProblematicKeyringError(
                "Keyring check failed!\n"
                "A problem was encountered when trying to load the keyring module:\n"
                "\n"
                "    No response was received within the specified timeout period.\n"
                "    Either the user didn't respond or the `keyring` module is freezing.\n"
                "\n"
                "* If the keyring module is freezing consider replacing the backend by setting"
                "  `PYTHON_KEYRING_BACKEND`. For example, the 'CryptFileKeyring' is a reliable"
                "  alternative and can be set via:\n"
                "\n"
                "    export PYTHON_KEYRING_BACKEND=keyrings.cryptfile.cryptfile.CryptFileKeyring;\n"
                "    export KEYRING_CRYPTFILE_PASSWORD=my_password;\n"
                "\n"
                "  For more information on configuring `keyring` visit the author's website:\n"
                "\n"
                "    https://github.com/jaraco/keyring."
                "\n"
                f"* If there wasn't enough time for the user to respond set `{__K_ENV_VAR_CHECK}` to a\n"
                f"  longer timeout. The value is in seconds and the default is 30.\n"
                "\n"
                f"* If this check isn't necessary set `{__K_ENV_VAR_CHECK}` to 0, to skip the check\n"
                f"  entirely." )


def __get_keyring():
    #
    # Problem 1: Enable and check DBUS
    #
    # Ubuntu's secret-storage needs DBUS, which in turn needs an event loop.
    # There is usually one already, but for some reason in Flask there isn't,
    # so we create one.
    import asyncio

    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop( loop )

    try:
        import keyring
    except ImportError as ex:
        raise RuntimeError(
                "The python 'keyring' package is not installed. "
                "This package should have been installed as a dependency of the current "
                "application, but you may be able to resolve this issue by installing the 'keyring' "
                "package manually and trying again. "
                "You may also encounter this error if you have directed the `keyring` package "
                "to defer to a keyring that is not itself installed." ) from ex

    #
    # Boilerplate code:
    # When using the 3rd party package keyrings.cryptfile
    # (keyrings.cryptfile.cryptfile.CryptFileKeyring), read the keyring password
    # from an environment variable.
    #
    if keyring.get_keyring().__class__.__name__ == "CryptFileKeyring":
        import os
        kr_password = os.getenv( __K_ENV_VAR_CRYPTFILE )

        if not kr_password:
            raise RuntimeError(
                    f"`CryptFileKeyring` is being used but the `{__K_ENV_VAR_CRYPTFILE}` environment variable has not been set. Please set this and try again. Use `-` to assume the `CryptFileKeyring` default behaviour (i.e. to prompt the user each time)." )

        if kr_password != "-":
            keyring.get_keyring().keyring_key = kr_password

        # Detect errors early - try to get a password now
    try:
        keyring.get_password( "test", "test" )
    except RuntimeError as ex:
        raise ProblematicKeyringError( "The python 'keyring' raised an error when trying to obtain a password. "
                                       "The `keyring` module may require manual configuration."
                                       "For more information see the author's website: https://github.com/jaraco/keyring." ) from ex

    return keyring


class ManagedPassword:
    """
    Stores a password in the system keyring.
    
    When saved via `__getstate__`, a randomly generated key is saved, and not
    the actual password. The actual password is saved to the system using this
    key.
    
    When loaded via `__setstate__`, the randomly generated key is loaded instead
    of the password. This is used to retrieve the password from the system.
    
    This behaviour may be overriden in the constructor.
    
    Note: This class now only writes the password to the system keyring if 
    __getstate__ has actually been called.
    
    :cvar DEFAULT_KEYRING: Name of the keyring used by this class. 
    """
    DEFAULT_KEYRING = "python_mhelper"

    def __init__( self, password, *, key = None, keyring = None, managed = True ):
        """
        Construct a new managed password.
        
        :param password:        The password (plaintext) 
        :param key:             Set to override the default behaviour of
                                randomly generating the key.
        :param keyring:         Set to override the keyring name.
                                This default is `DEFAULT_KEYRING`.
        :param managed:         Setting this flag to `False` forgoes managing
                                the password entirely, the password will be
                                both stored and restored as plain text. Useful
                                only to emulate class behaviour without managing
                                the password.
        """
        if not key:
            import uuid
            key = str( uuid.uuid4() )

        if not keyring:
            keyring = "mhelper.password_helper"

        self.__key = key
        self.__keyring = keyring
        self.__password = password
        self.__managed = managed
        self.__is_saved = False
        self.__is_loaded = True

    @property
    def key( self ) -> str:
        """
        The key. 
        """
        return self.__key

    @property
    def keyring( self ) -> str:
        """
        The keyring (typically the service name).
        """
        return self.__keyring or self.DEFAULT_KEYRING

    @property
    def password( self ) -> str:
        """
        Obtains the password plaintext.
        
        Note: If the password is removed from the system (and this class doesn't
        know about it), the retrieved password will be blank.
        """
        self.__load()
        return self.__password

    def __load( self ):
        if self.__is_loaded:
            return

        if not self.__managed:
            assert self.__password is not None, "Logic error, unmanaged password but no password is specified."
            return self.__password

        assert self.__password is None, "Password is already loaded."
        keyring = get_keyring()
        self.__password = keyring.get_password( self.keyring, self.key )

        if self.__password is None:
            self.__password = ""

        self.__is_loaded = True

    def __save( self ):
        if self.__is_saved:
            return

        self.__is_saved = True

        if not self.__managed:
            return

        keyring = get_keyring()
        keyring.set_password( self.keyring, self.key, self.__password )

    def delete( self ):
        """
        Deletes the entry in the keyring associated with the password.
        """
        if not self.__key:
            raise ValueError( "Logic error, attempt to delete a password that is already deleted." )

        if self.__managed:
            if self.__is_saved:
                keyring = get_keyring()
                keyring.delete_password( self.keyring, self.key )

        self.__key = None
        self.__keyring = None
        self.__password = None
        self.__managed = False

    def __setstate__( self, state: Dict[str, object] ) -> None:
        """
        Restores the state of the object.
        """
        self.__key = state["key"]
        self.__keyring = state["keyring"]
        self.__password = state["password"]
        self.__managed = state["managed"]
        self.__is_saved = True
        self.__is_loaded = False

    def __getstate__( self ) -> Dict[str, object]:
        """
        Stores the state of the object.
        The password plaintext will not be available unless `managed` is unset.
        """
        self.__save()
        return { "key"     : self.__key,
                 "keyring" : self.__keyring,
                 "managed" : self.__managed,
                 "password": self.password if not self.__managed else None }

    def __repr__( self ):
        """
        Representation displays the key and not the password.
        """
        return "{}(key={},keyring={})".format( type( self ).__name__, repr( self.__key ), repr( self.__keyring ) )

    def __str__( self ):
        """
        String conversion displays asterisks only.
        """
        return "********"


def get_password( service_name: str, user_name: str ) -> Optional[str]:
    return get_keyring().get_password( service_name, user_name )


def set_password( service_name: str, user_name: str, password: str ) -> None:
    return get_keyring().set_password( service_name, user_name, password )


def get_invocation( service_name, user_name ) -> str:
    import sys
    return (f"Missing password.\n"
            f"******************************* MISSING PASSWORD *******************************\n"
            f"* \n"
            f"* KEYRING: {get_backend()}\n"
            f"* Invoke the following command to configure the password:\n"
            f"* \n"
            f'*     "{sys.executable}" "{__file__}" --set {service_name} {user_name}\n'
            f"* \n"
            f"********************************************************************************\n")


def autogenerate_password( service_name:str, user_name:str )->str:
    password = get_password( service_name, user_name )

    if not password:
        import warnings
        import secrets
        import sys
        warnings.warn( (f"Autogenerated password.\n"
                        f"******************************* AUTOGENERATED PASSWORD *******************************\n"
                        f"* \n"
                        f"* No password has been configured. I'm created one for you\n"
                        f"* Invoke the following command if you want to change it:\n"
                        f"* \n"
                        f'*     "{sys.executable}" "{__file__}" --set {service_name} {user_name}\n') )
        password = secrets.token_urlsafe()
        set_password( service_name, user_name, password )

    return password


def __test__():
    keyring = get_keyring()

    s = "mjr_test_service"
    u = "mjr_username"
    p = "mjr_password"

    keyring.set_password( s, u, p )
    r = keyring.get_password( s, u )

    if not r:
        raise RuntimeError( "Password not saved." )

    if r != p:
        raise RuntimeError( "Retrieved password does not match original." )

    keyring.delete_password( s, u )

    if keyring.get_password( s, u ) is not None:
        raise RuntimeError( "Password not deleted." )

    mp = ManagedPassword( p )

    state = mp.__getstate__()

    if state["password"] is not None:
        raise RuntimeError( "Password visible in plain text." )

    rs = ManagedPassword.__new__( ManagedPassword )
    rs.__setstate__( state )

    if not rs.password:
        raise RuntimeError( "ManagedPassword not saved." )

    if rs.password != p:
        raise RuntimeError( "ManagedPassword does not match original." )

    rs.delete()
    print( "Testing complete." )


def get_backend() -> str:
    return get_keyring().get_keyring().__class__.__name__


def main():
    import sys
    a = sys.argv
    a0 = sys.argv[1].lstrip( "-" ) if len( a ) > 1 else None

    if len( a ) == 2 and a0 in ("t", "test",):
        return __test__()
    elif len( a ) == 2 and a0 == "check":
        __get_keyring()
        return 0
    elif len( a ) == 4 and a0 in ("g", "get",):
        keyring = get_keyring()
        pw = keyring.get_password( a[2], a[3] )

        if pw is None:
            print( f"No such password." )
        else:
            print( f"Read: {pw!r}" )

        return 0
    elif len( a ) in (4, 5) and a0 in ("s", "set",):
        pw2 = None
        if len( a ) == 4:
            import getpass
            print( "********************************************************************************",
                   file = sys.stderr )
            print( "This command will add a password to the keyring.", file = sys.stderr )
            print( "", file = sys.stderr )
            print( f"    KEYRING : {get_backend()}", file = sys.stderr )
            print( f"    SERVICE : {a[2]}", file = sys.stderr )
            print( f"    USERNAME: {a[3]}", file = sys.stderr )
            print( "", file = sys.stderr )
            print( "********************************************************************************",
                   file = sys.stderr )
            print( "", file = sys.stderr )
            print( "Enter the new password and then optionally confirm it.", file = sys.stderr )
            print( "Enter a blank password to cancel.", file = sys.stderr )
            print( "", file = sys.stderr )
            pw = getpass.getpass( "Password: " )

            if pw:
                pw2 = getpass.getpass( " confirm: " )

                if pw2 and pw2 != pw:
                    print( "Mismatch.", file = sys.stderr )
                    return 1
        else:
            pw = a[4]

        if not pw:
            print( "Cancelled.", file = sys.stderr )
            return 0

        keyring = get_keyring()
        keyring.set_password( a[2], a[3], pw )

        if pw2:
            print( "Confirmed, written.", file = sys.stderr )
        else:
            print( "Not confirmed, written.", file = sys.stderr )
            
        if keyring.get_password( a[2], a[3] ) == pw:
            print( "Saved OK.", file = sys.stderr )
        else:
            print( "ERROR: Not saved.", file = sys.stderr )
            
        return 0
    elif len( a ) == 4 and a0 in ("d", "del", "delete"):
        keyring = get_keyring()
        keyring.delete_password( a[2], a[3] )
        print( "Deleted.", file = sys.stderr )
        return 0
    else:
        print( __doc__, file = sys.stderr )
        return 1


if __name__ == "__main__":
    main()
