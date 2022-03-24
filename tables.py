from descriptors import UnsignedInteger, UnsignedFloat, SizedString, Date, Installments


class Register():
    table_name   = 'register'
    user_id      = UnsignedInteger('user_id')
    date         = Date('date')
    purchase_id  = SizedString('purchase_id', size=32)
    installments = Installments('installments')
    price        = UnsignedFloat('price')

    def __init__(self, user_id, date, purchase_id, installments, price):
        self.user_id      = user_id
        self.date         = date 
        self.purchase_id  = purchase_id
        self.installments = installments
        self.price        = price
        
    
class User():
    table_name = 'user'
    name       = SizedString('name', size=32) 
    debt       = UnsignedFloat('debt') 
    paid_out   = UnsignedFloat('paid_out')  

    def __init__(self, name, debt, paid_out):
        self.name     = name
        self.debt     = debt
        self.paid_out = paid_out