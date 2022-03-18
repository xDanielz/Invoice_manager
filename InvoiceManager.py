import DataBaseManager
from validationstools import *
from InvoiceExceptions import *


class InvoiceManager(DataBaseManager):

    def __init__(self, dbname, tablename) -> None:
        super().__init__(dbname, tablename)
        self.id_val = id_validator(dbname, tablename='USERS')

    def save(self, user_id, date, purchase_id, installments, price):

        if not self.id_val(user_id):
            raise InvalidId('campo "user_id" inválido')

        if not date_validator(date):
            raise InvalidDate('campo "date" inválida')

        if not installments_validator(installments):
            raise InvalidInstallments('campo "installments" inválido')

        if not isinstance(price, float):
            raise ValueError('campo "price" inválido')
        
        super().save({
            'user_id'     :user_id,
            'date'        :date,
            'purchase_id' :purchase_id,
            'installments':installments,
            'price'       :price
            })
            
    def delete(self, user_id):
        pass 

    def update(self, user_id, date=None, purchase_id=None, installments=None, price=None):
        pass

    def view(self, user_id, date=None, purchase_id=None, installments=None, price=None):
        pass


class UserManager(DataBaseManager):

    def __init__(self, dbname, tablename) -> None:
        super().__init__(dbname, tablename)

    def save(self, name, debt, paid_out):
        pass

    def delete(self, user_id):
        pass

    def update(self, user_id, debt=None, paid_out=None):
        pass

    def view(self):
        pass  