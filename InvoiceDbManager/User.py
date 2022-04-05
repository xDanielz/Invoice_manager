from .UseSqlite3db import *

exc      = cursor_exc('INVOICE')
id_exist = colunm_exist('INVOICE', 'User')


def save(name: str):
    sql = '''INSERT INTO User VALUES(NULL, ?, 0)'''
    exc(sql, (name,))


def change_name(_id: int, name: str):
    id_exist('Id', _id)
    sql = '''UPDATE User SET Name = ? WHERE Id = ?'''
    exc(sql, (name, _id))


def increase_balance(_id: int, value: float):
    id_exist('Id', _id)    
    sql = '''UPDATE User SET Paid_out = Paid_out + ? WHERE Id = ?'''
    exc(sql, (value, _id))


def decrease_balance(_id: int, value: float):
    id_exist('Id', _id)
    sql = '''UPDATE User SET Paid_out = Paid_out - ? WHERE Id = ?'''
    exc(sql, (value, _id))


def delete(_id: int):
    id_exist('Id', _id)
    sql = '''DELETE FROM User WHERE Id = ?'''
    exc(sql, (_id,))


def view_users():
    sql = '''SELECT * FROM User'''
    with UseSqlite3db('INVOICE') as cursor:
        data = cursor.execute(sql)
        return data.fetchall()
