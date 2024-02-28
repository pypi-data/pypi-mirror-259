"""
Provides DB functions
"""
import sqlite3
from sqlite3 import Cursor


class DB():
    """
    Only need to instantiate once, not dependant on specific DB 
    you are accessing 
    """
    cursor: Cursor

    def __init__(self) -> None:
        pass

    def instantiate_sqlite_table(self, file_name: str) -> sqlite3.Cursor:
        """Sets up the required sqlite db"""
        con = sqlite3.connect(file_name)
        cur = con.cursor()
        res = cur.execute("SELECT ? FROM sqlite_master", ('music',))
        is_created = res.fetchone()
        if is_created is None:
            cur.execute("CREATE TABLE music(mtime, file_path type UNIQUE)")
        self.cursor = cur
        return cur

    def db_get_all(self) -> list:
        """Returns all values from the current db"""
        res = self.cursor.execute("SELECT * FROM music")
        ret_val = res.fetchall()
        return [] if ret_val is None else ret_val

    def db_insert(self, entry: tuple):
        """Places an entry into the db with two values
        mtime and file_path from the tuple
        will match on file_path to update existing rows"""
        sub_obj = {
            'mtime': entry[0],
            'file_path': entry[1]
        }
        self.cursor.execute("""
                    INSERT INTO music(mtime,file_path) 
                    VALUES (:mtime, :file_path) 
                    ON CONFLICT(file_path) 
                    DO UPDATE SET mtime=:mtime, file_path=:file_path
                    """,
                            sub_obj)

    def db_delete(self) -> None:
        """Performs a delete on all rows in the music db"""
        self.cursor.execute("DELETE FROM music")

    def db_commit(self) -> None:
        """Commits all outstanding statements"""
        self.cursor.connection.commit()

    def db_close(self) -> None:
        """Closes the connection"""
        self.cursor.connection.close()
