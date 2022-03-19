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

    def validation(self, **kwargs):
        return super().validation(**kwargs)


class UserManager(InvoiceManager):
    def __init__(self) -> None:
        self._TABLE_NAME = 'users'
        super().__init__(self._TABLE_NAME)

    def view(self):
        super().view_all()

    def validation(self, **kwargs):
        pass  