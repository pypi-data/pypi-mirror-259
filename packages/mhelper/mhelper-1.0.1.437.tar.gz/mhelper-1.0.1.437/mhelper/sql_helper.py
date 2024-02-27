"""
Manages a MySQL database connection.

`MySQLdb`, from `mysqlclient` is required

`mysqlclient` may not be installed by the application itself because it has issues being installed on some systems
that would otherwise prevent the application being installed.

`mysqlclient` can be installed manually::

    python -m pip install mysqlclient

"""
# !REQUIRE  
import subprocess
from typing import Optional, Tuple, Union
from mhelper.disposal_helper import ManagedWith, IWith
from mhelper import io_helper
import os
import sys

try:
    # noinspection PyPackageRequirements
    import MySQLdb
except ImportError:
    MySQLdb = OperationalError = IntegrityError = None  # required for intellij
    raise ImportError( f"\n"
                       f"*******************************************************************************\n"
                       f"* MISSING DEPENDENCY                                                          *\n"
                       f"*******************************************************************************\n"
                       f"*                                                                             *\n"
                       f"* `mysqlclient` is required for this package to run. Please install this      *\n"
                       f"* package and try again. See the documentation in the following file for more *\n"
                       f"* details:                                                                    *\n"
                       f"*                                                                             *\n"
                       f"*    {__file__}\n"
                       f"*                                                                             *\n"
                       f"* You can install the `mysqlclient` manually by running:                      *\n"
                       f"*                                                                             *\n"
                       f"*    {sys.executable} -m pip install mysqlclient\n"
                       f"*                                                                             *\n"
                       f"*******************************************************************************\n" )

# noinspection PyPackageRequirements,PyUnresolvedReferences
from MySQLdb import OperationalError, IntegrityError
# noinspection PyPackageRequirements,PyUnresolvedReferences
from MySQLdb.cursors import Cursor


class Remote:
    """
    Describes a remote server and contains a few methods for dealing with it.
    """

    def __init__( self,
                  *,
                  user_name: str,
                  password: Optional[str] = None,
                  password_key: Union[None, Tuple[str, str], str] = None,
                  host: Optional[str] = None,
                  port: Optional[int] = None,
                  db_name: str ):
        """
        :param user_name:       Username
                                Required.
                                
        :param password:        Password.
                                Optional, defaults to using `password_key`.
                                  
        :param password_key:    The key used to the password from the keyring.
                                Used only if `password` is not set.
                                Optional, defaults to `None`.
                                
                                * `None`    --> Automatic application name, automatic user name.
                                * `str`     --> Specified application name, automatic user name.
                                * `tuple`   --> Specified application name, specified user name.
                                
        :param host:            Host.
                                Optional, defaults to "localhost".
        :param port:            Port.
                                Optional, defaults to MySQL default (3306).
        :param db_name:         Database to use.
                                Required.
        :exception ValueError:  No such password with key. 
        """
        if not host:
            host = "localhost"

        self.user_name = user_name
        self.__password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.password = self.__acquire_password( password_key, password )
        
    def __repr__(self):
        return f"{type(self).__name__}({self.user_name}@{self.host}:{self.port} {self.db_name})"

    def __acquire_password( self, password_key, password ):
        if password:
            return password

        password_key = password_key or "mhelper.sql_helper"

        if isinstance( password_key, str ):
            port_ = f":{self.port}" if self.port else ""
            password_key_t = password_key, f"{self.user_name}@{self.host}{port_}:{self.db_name}"
        else:
            password_key_t = password_key

        from mhelper import password_helper
        password = password_helper.get_password( *password_key_t )

        if not password:
            raise ValueError( password_helper.get_invocation( *password_key_t ) )

        return password

    def connect( self, **kwargs ) -> IWith["_ConnectionProtocol"]:
        """
        Connects to the server.
        """
        return ManagedWith( self.__get_connection( **kwargs ),
                            on_exit = lambda c: c.close() )

    def __get_connection( self, db = True ):
        return MySQLdb.connect( host = self.host,
                                user = self.user_name,
                                passwd = self.password,
                                **({ "port": self.port } if self.port else { }),
                                **({ "database": self.db_name } if db else { }) )

    def drop_database( self, missing_ok: bool = True ) -> bool:
        if missing_ok:
            if not self.db_exists():
                return False

        with self.connect( db = False ) as db:
            with db.cursor() as csr:
                csr.execute( f"DROP DATABASE {self.db_name}" )

            db.commit()

        return True

    def create_database( self, exists_ok: bool = False ) -> bool:
        if exists_ok:
            if self.db_exists():
                return False

        with self.connect( db = False ) as db:
            with db.cursor() as csr:
                csr.execute( f"CREATE DATABASE {self.db_name} CHARACTER SET utf8 COLLATE utf8_bin" )

            db.commit()

        return True

    def create_table( self, table_name: str, sql: str ):
        self.create_database()

        with self.connect() as con:
            with con.cursor() as csr:
                csr.execute( f"SHOW TABLES LIKE '{table_name}'" )

                row = csr.fetchone()

                if row is not None:
                    return

                csr.execute( sql )

            con.commit()

    def execute_file( self, file_name: str ) -> None:
        """
        :param file_name: 
        :return: 
        
        :exception FileNotFoundError:  Cannot find `mysql`.
                                       Cannot find `file_name`.
        """
        cmd = ["mysql",
               "-u", self.user_name,
               f'-p{self.password}',
               "--host", self.host,
               *(["--port", str( self.port )] if self.port else []),
               self.db_name]

        if not os.path.isfile( file_name ):
            raise FileNotFoundError( f"The SQL source file `{file_name}` does not exist." )

        if file_name.endswith( ".gz" ):
            ungz_file = io_helper.ungzip( file_name, overwrite = False )
            self.execute_file( ungz_file )
            return

        with open( file_name ) as fin:
            try:
                p = subprocess.Popen( cmd, stdin = fin, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
                so, se = p.communicate()
                assert p.returncode is not None
                r = p.returncode
            except FileNotFoundError:
                raise FileNotFoundError(
                        f"Cannot find `mysql`. Please make sure this executable is available on the PATH and try again." )

            if r:
                raise RuntimeError(
                        f"Bad return code {r} from process: {' '.join( cmd )} < {file_name}\n\n" + so.decode(
                                "utf8" ) + "\n\n" + se.decode( "utf8" ) )

    def db_exists( self ) -> bool:
        with self.connect( db = False ) as db:
            with db.cursor() as csr:
                csr.execute( "SHOW DATABASES" )
                return (self.db_name,) in csr

    def get_directory( self ) -> Optional[str]:
        SQL = 'SHOW VARIABLES WHERE Variable_Name = "datadir"'

        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute( SQL )

                row = cursor.fetchone()

                if row is None:
                    return None

                path = row[-1]
                return os.path.join( path, self.db_name )


def now_sql() -> str:
    import datetime
    return datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )


# noinspection PyUnreachableCode
if False:
    from typing import Protocol


    class _ConnectionProtocol( Protocol, MySQLdb._mysql.connection ):
        def cursor( self, *args, **kwargs ) -> "MySQLdb.cursors.Cursor":
            pass
