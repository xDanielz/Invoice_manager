from descriptors import UnsignedInteger, UnsignedFloat, SizedString, Date, Installments
import DataBaseManager


class DbManager(DataBaseManager):

    def __init__(self, obj, dbname) -> None:
        self.obj = obj
        self.dbname = dbname 
        self.table_name = obj.table_name
        super().__init__(self.dbname, self.table_name)

    def save(self):
        super().save(**self.obj.__dict__)
            
    def delete(self, _id):
        super().delete(_id)

    def update(self, _id):
        super().update(_id, **self.obj__dict__)

    def view(self):
        return super().view(**self.obj.__dict__)



class Register():
    table_name   = 'register'
    user_id      = UnsignedInteger()
    date         = Date()
    purchase_id  = SizedString(size=32)
    installments = Installments()
    price        = UnsignedFloat()

    def __init__(self, user_id, date, purchase_id, installments, price):
        self.user_id      = user_id
        self.date         = date 
        self.purchase_id  = purchase_id
        self.installments = installments
        self.price        = price
        
    
class User():
    table_name = 'user'
    name       = SizedString(size=32) 
    debt       = UnsignedFloat() 
    paid_out   = UnsignedFloat()  

    def __init__(self, name, debt, paid_out):
        self.name     = name
        self.debt     = debt
        self.paid_out = paid_out