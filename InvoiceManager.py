import sqlite3
import DataBaseManager
from validationstools import *
from InvoiceExceptions import *


DATA_BASE_NAME = 'INVOICE'
id_val = id_validator(DATA_BASE_NAME)

class InvoiceManager(DataBaseManager):

    def __init__(self, table_name) -> None:
        self._TABLE_NAME = table_name
        super().__init__(DATA_BASE_NAME, self._TABLE_NAME)

    def save(self, **kwargs):
        self.validation(**kwargs)
        super().save(**kwargs)
            
    def delete(self, _id):
        if not id_val(_id, self._TABLE_NAME):
            raise InvalidId('campo "id" inválido')
        super().delete(_id)

    def update(self, _id, **kwargs):
        self.validation(**kwargs)
        super().update(_id, **kwargs)

    def view(self, **kwargs):
        self.validation(**kwargs)
        return super().view(**kwargs)

    def validation(self, **kwargs):
        pass


class RegisterManager(InvoiceManager):
    def __init__(self) -> None:
        self._TABLE_NAME = 'register'
        super().__init__(self._TABLE_NAME)
        try:
            self.excsql('''
                CREATE TABLE register(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    date VARCHAR(10) NOT NULL,
                    purchase_id VARCHAR(100) NOT NULL,
                    installments VARCHAR(5) NOT NULL,
                    price REAL NOT NULL,
                    FOREIGN KEY (users) REFERENCES users(id)
                )
            ''')
        except sqlite3.OperationalError:
            pass 

    def validation(self, **kwargs):
        if 'user_id' in kwargs:               
            if not id_val(kwargs['user_id'], 'users'):
                raise InvalidId('campo "user_id" inválido')
        if 'date' in kwargs:            
            if not date_validator(kwargs['date']):
                raise InvalidDate('campo "date" inválida')
        if 'installments' in kwargs:            
            if not installments_validator(kwargs['installments']):
                raise InvalidInstallments('campo "installments" inválido')
        if 'price' in kwargs:            
            if not float_validator(kwargs['price']):
                raise ValueError('campo "price" inválido')


class UserManager(InvoiceManager):
    def __init__(self) -> None:
        self._TABLE_NAME = 'users'
        super().__init__(self._TABLE_NAME)

    def view(self):
        super().view_all()

    def validation(self, **kwargs):
        for attr in 'debt', 'paid':
            if attr in kwargs:               
                if not float_validator(kwargs[attr]):
                    raise ValueError(f'campo {attr} inválido') 