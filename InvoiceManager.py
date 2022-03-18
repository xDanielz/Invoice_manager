import DataBaseManager
from validationstools import *


class InvoiceManager(DataBaseManager):

    def save(self, user_id, date, purchase_id, installments, price):
        if not id_validator(user_id):
            pass
        if not date_validator(date):
            pass
        if not installments_validator(installments):
            pass
        if not isinstance(price, float):
            pass
        
            
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

    def save(self, name, debt, paid_out):
        pass

    def delete(self, user_id):
        pass

    def update(self, user_id, debt=None, paid_out=None):
        pass

    def view(self):
        pass  