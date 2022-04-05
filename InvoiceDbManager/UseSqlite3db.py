import sqlite3


class UseSqlite3db:
    def __init__(self, *config):
        self.configuration = config

    def __enter__(self):
        self.conn = sqlite3.connect(*self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def cursor_exc(dbname: str) -> 'function':
    assert isinstance(dbname, str)

    def func(*args):
        with UseSqlite3db(dbname) as cursor:
            cursor.execute(*args)

    return func

def colunm_exist(dbname, tablename):
    def func(colunm_name, value):
        with UseSqlite3db(dbname) as cursor:
            sql = f'''SELECT {colunm_name} FROM {tablename} WHERE {colunm_name} = {value}'''
            data = cursor.execute(sql).fetchone()
            if data is None:
                raise ValueError(f'{colunm_name} {value} Inexistente') 
    return func

