from .DataBaseManager import cursor_exc


DATABASE_NAME = "INVOICE"
exc = cursor_exc(DATABASE_NAME)

try:
    exc('''
        CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) UNIQUE NOT NULL,
            debt REAL NOT NULL,
            paid_out REAL NOT NULL)
    ''')
except:
    pass 

try:
    exc('''
        CREATE TABLE register(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES user(id) NOT NULL,
            date VARCHAR(10) NOT NULL,
            purchase_id VARCHAR(100) NOT NULL,
            installments VARCHAR(5),
            price REAL NOT NULL)
    ''')
except:
    pass  
