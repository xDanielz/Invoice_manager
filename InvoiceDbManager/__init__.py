from .UseSqlite3db import cursor_exc


exc = cursor_exc('INVOICE')

try:
    exc('''
        CREATE TABLE User(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) UNIQUE NOT NULL,
            Paid_out REAL NOT NULL)
    ''')
except:
    pass 

try:
    exc('''
        CREATE TABLE Register(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            UserID INTEGER REFERENCES User(Id) NOT NULL,
            Date DATE NOT NULL,
            PurchaseID VARCHAR(100) NOT NULL,
            Installments VARCHAR(5),
            Price REAL NOT NULL)
    ''')
except:
    pass 