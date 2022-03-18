from datetime import datetime
from UseSqlite3db import UseSqlite3db


def id_validator(dbname, tablename):

    def func(_id):
        sql = f'SELECT FROM {tablename} * WHERE ID=?'
        with UseSqlite3db(dbname) as cursor:
            result = cursor.execute(sql, _id)
            
            return result is None
    return func

def date_validator(date):
    try:
        datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        return 0
    
    return 1
