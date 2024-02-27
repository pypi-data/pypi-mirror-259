"""

"""
# !REQUIRE werkzeug
# !REQUIRE mhelper.sql_helper
import datetime
from functools import lru_cache
from typing import Optional

from mhelper import sql_helper
# noinspection PyPackageRequirements
from werkzeug import security


TABLE_NAME = "mhuh_users"
SQL = f"""
                    create table {TABLE_NAME}
                    (
                        id int auto_increment,
                        name CHAR(50) not null,
                        password VARCHAR(255) not null,
                        data TEXT not null,
                        updated DATETIME not null,
                        constraint users_pk
                            primary key (id)
                    );
                    
                    create unique index users_id_uindex
                        on users (id);
                    
                    create unique index users_username_uindex
                        on users (name);
                    """

class UsersDb:
    
    
    def __init__( self, remote: sql_helper.Remote ):
        self.remote = remote
        
        self.remote.create_database()
        self.remote.create_table(TABLE_NAME, SQL)
    
    
    @lru_cache
    def get_user_name( self, user_id: int ) -> Optional[str]:
        try:
            with self.remote.connect() as con:
                with con.cursor() as cursor:
                    cursor: sql_helper.Cursor
                    sql = f"SELECT `name` FROM `{TABLE_NAME}` WHERE `id` = %s"
                    args = [user_id]
                    cursor.execute( sql, args )
                    
                    row = cursor.fetchone()
                    
                    if not row:
                        return None
                    
                    user_name = row[0]
                    
                    return user_name
        except Exception:
            return None
    
    
    def register_user( self, name, password ):
        updated = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )
        password_hash = security.generate_password_hash( password )
        data = ""
        
        with self.remote.connect() as con:
            with con.cursor() as cursor:
                sql = f"INSERT INTO `{TABLE_NAME}` (`name`, `password`, `data`, `updated`) VALUES (%s, %s, %s, %s)"
                args = (name, password_hash, data, updated)
                
                try:
                    cursor.execute( sql, args )
                except sql_helper.IntegrityError:
                    # Duplicate
                    return False
                
                con.commit()
        
        return True
    
    
    def check_user( self, name, password ) -> Optional[int]:
        updated = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )
        
        try:
            with self.remote.connect() as con:
                with con.cursor() as cursor:
                    cursor: sql_helper.Cursor
                    sql = f"SELECT `id`, `password` FROM `{TABLE_NAME}` WHERE `name` = %s"
                    args = [name]
                    cursor.execute( sql, args )
                    
                    row = cursor.fetchone()
                    
                    if not row:
                        return None
                    
                    user_id = row[0]
                    password_hash = row[1]
                    
                    if not security.check_password_hash( password_hash, password ):
                        return False
                    
                    sql = f"UPDATE `{TABLE_NAME}` SET `updated` = %s WHERE `id` = %s"
                    args = [updated, user_id]
                    cursor.execute( sql, args )
                    
                    con.commit()
                    
                    return user_id
        except Exception:
            return None
