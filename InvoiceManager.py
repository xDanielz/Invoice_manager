import DataBaseManager


class InvoiceManager(DataBaseManager):
    def __init__(self, dbname: str, tablename: str) -> None:
        super().__init__(dbname, tablename)

    def save(self, user_id, date, purchase_id, installments, price):
        pass

    def delete(self, user_id):
        pass

    def update(self, user_id, date=None, purchase_id=None, installments=None, price=None):
        pass

    def view(self, user_id, date=None, purchase_id=None, installments=None, price=None):
        pass


class UserManager(DataBaseManager):
    def __init__(self, dbname: str, tablename: str) -> None:
        super().__init__(dbname, tablename)

    def save(self, name, debt, paid_out):
        pass

    def delete(self, user_id):
        pass

    def update(self, user_id, debt=None, paid_out=None):
        pass

    def view(self):
        pass  