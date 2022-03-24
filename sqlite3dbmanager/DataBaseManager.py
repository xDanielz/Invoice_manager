from .UseSqlite3db import *


class DataBaseManager:

    def __init__(self, dbname: str, tablename: str):
        self.dbname    = dbname
        self.tablename = tablename
        self.excsql    = cursor_exc(dbname)

    def save(self, **kwargs):
        sql = ''' INSERT INTO {tablename} ({keys}) VALUES ({values}) '''

        sql = sql.format(
                tablename = self.tablename,
                keys = ','.join(kwargs.keys()),
                values = ','.join('?' for _ in range(len(kwargs)))
        )
        
        self.excsql(sql, list(kwargs.values()))

    def delete(self, _id):
        sql = ''' DELETE FROM {tablename} WHERE ID = ? '''
        sql = sql.format(tablename = self.tablename)
        self.excsql(sql, (_id,))

    def update(self, _id, **kwargs):
        sql = ''' UPDATE {tablename} SET {attrs} WHERE ID = ? '''
        attrs = []

        for k in kwargs:
            attrs.append(f'{k}=?')

        sql = sql.format(
                tablename = self.tablename,
                attrs = ','.join(attrs)
        )

        self.excsql(sql, (*list(kwargs.values()), _id))


    def view(self, **kwargs):
        sql = ''' SELECT * FROM {tablename} WHERE {attrs} '''
        attrs = []

        for k in kwargs:
            attrs.append(f'{k}=?')

        sql = sql.format(
                tablename = self.tablename,
                attrs = ','.join(attrs)
        )	

        with UseSqlite3db(self.dbname) as cursor:
            data = cursor.execute(sql, list(kwargs.values()))
            return data.fetchall()
    
    def view_all(self):
        sql = ''' SELECT * FROM {tablename} '''
        sql = sql.format(tablename = self.tablename)

        with UseSqlite3db(self.dbname) as cursor:
            data = cursor.execute(sql)
            return data.fetchall()
