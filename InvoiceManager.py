import DataBaseManager
from validationstools import *
from InvoiceExceptions import *


DATA_BASE_NAME = 'INVOICE'
id_val = id_validator(DATA_BASE_NAME)

class InvoiceManager(DataBaseManager):

    def __init__(self) -> None:
        _TABLE_NAME = 'invoice'
        super().__init__(DATA_BASE_NAME, _TABLE_NAME)

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
        super().view(**kwargs)

    def validation(**kwargs):
        if 'user_id' in kwargs:               
            if not id_val(kwargs['user_id'], 'users'):
                raise InvalidId('campo "user_id" inválido')
        if 'date' in kwargs:            
            if not date_validator(kwargs['date']):
                raise InvalidDate('campo "date" inválida')
        if 'installments' in kwargs:            
            if not installments_validator(['installments']):
                raise InvalidInstallments('campo "installments" inválido')
        if 'price' in kwargs:            
            if not isinstance(kwargs['price'], float):
                raise ValueError('campo "price" inválido')

class UserManager(DataBaseManager):

    def __init__(self) -> None:
        _TABLE_NAME = 'users'
        super().__init__(DATA_BASE_NAME, _TABLE_NAME)

    def save(self, **kwargs):
        pass

    def delete(self, _id):
        pass

    def update(self, **kwargs):
        pass

    def view(self):
        super().view_all()

    def validation(self, kwargs):
        pass  