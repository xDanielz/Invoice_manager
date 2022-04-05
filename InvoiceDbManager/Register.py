from .UseSqlite3db import *


exc = cursor_exc('INVOICE')
id_exist = colunm_exist('INVOICE', 'Register')
user_id_exist = colunm_exist('INVOICE', 'User')


def save(user_id: int, date: str, purchase_id: str, installments: str, price: float):
        user_id_exist('Id', user_id)
        sql = '''INSERT INTO Register VALUES(NULL, ?, ?, ?, ?, ?)'''
        exc(sql, (user_id, date, purchase_id, installments, price))

def update(_id: int, **kwargs):
        id_exist('Id', _id)
        sql = '''UPDATE Register SET {attrs} WHERE Id = ?'''
        attrs = []

        for k in kwargs:
            attrs.append(f'{k}=?')

        sql = sql.format(attrs = ','.join(attrs))
        exc(sql, (*list(kwargs.values()), _id))

def delete(_id: int):
        id_exist('Id', _id)
        sql = '''DELETE FROM Register WHERE Id = ?'''
        exc(sql, (_id,))

def view_all():
        sql = '''SELECT Register.ID, User.Name, Register.Date, Register.PurchaseID, Register.Installments, Register.Price 
                 FROM Register 
                 INNER JOIN User ON Register.UserID = User.Id'''

        with UseSqlite3db('INVOICE') as cursor:
            data = cursor.execute(sql)
            return data.fetchall()

def filtered_view(name=None, _id=None):
        attr = _id 
        sql  = '''SELECT *
                  FROM Register
                  WHERE ID = ?'''

        if name is not None:
            attr = name
            sql  = '''SELECT Register.ID, Register.Date, Register.PurchaseID, Register.Installments, Register.Price 
                      FROM Register
                      INNER JOIN User ON Register.UserID = User.Id 
                      WHERE User.Name LIKE ?'''
        

        with UseSqlite3db('INVOICE') as cursor:
            data = cursor.execute(sql, (attr,))
            return data.fetchall()

def view_register_summary():
        sql = '''SELECT User.Name, SUM(Register.Price), User.Paid_out 
                 FROM Register 
                 INNER JOIN User ON Register.UserID = User.Id GROUP BY UserID'''

        with UseSqlite3db('INVOICE') as cursor:
            data = cursor.execute(sql)
            return data.fetchall()