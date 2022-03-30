from descriptors import UnsignedInteger, UnsignedFloat, SizedString, Date, Installments
from sqlite3dbmanager.DataBaseManager import DataBaseManager


class UserManager(DataBaseManager):

    def __init__(self):
        self.register = DataBaseManager('INVOICE', 'register')
        super().__init__('INVOICE', 'user')

    def save(self, **kwargs):
        kwargs['debt']     = float(kwargs['debt'])
        kwargs['paid_out'] = float(kwargs['paid_out'])
        User(**kwargs)
        super().save(**kwargs)
        pass

    def update(self, _id, **kwargs):
        #Atualizando registro

        test_dict = {'name'     : 'teste', 
                     'debt'     : .0, 
                     'paid_out' : .0, 
                     }

        test_dict.update(kwargs)
        test_dict['debt']     = float(test_dict['debt'])
        test_dict['paid_out'] = float(test_dict['paid_out'])
        User(**test_dict)
        super().update(_id, **kwargs)

    def delete(self, _id):
        registers = self.register.view(user_id=_id)
        for reg in registers:
            self.register.delete(reg[0])
        super().delete(_id) 


class RegisterManager(DataBaseManager):
    
    def __init__(self):
        super().__init__('INVOICE', 'register')
        self.user = UserManager()
    
    def save(self, **kwargs):
        kwargs['price']   = float(kwargs['price'])
        kwargs['user_id'] = int(kwargs['user_id'])
        Records(**kwargs)
        user_id  = kwargs['user_id'] 
        price    = kwargs['price']
        reg_user = self.user.view(id=user_id)[0]
        debt     = float(reg_user[2]) + price
        #Salvando o registro
        super().save(**kwargs)
        #Atualizando o débito
        self.user.update(user_id, debt=debt)

    def delete(self, _id):
        reg      = self.view(id=_id)[0]
        price    = reg[-1]
        reg_user = self.user.view(id=reg[1])[0]
        debt     = reg_user[2] - price 
        #Apagando registro
        super().delete(_id)
        #Atualizando o débito
        self.user.update(reg_user[0], debt=debt)

    def update(self, _id, **kwargs):
        #Atualizando registro

        test_dict = {'user_id'     :  0, 
                     'date'        : '01/01/2001', 
                     'purchase_id' : 'teste', 
                     'installments': '01/01', 
                     'price'       :  .0}

        test_dict.update(kwargs)
        test_dict['price']   = float(test_dict['price'])
        test_dict['user_id'] = int(test_dict['user_id']) 
        Records(**test_dict) #Validando os dados
        reg          = self.view(id=_id)[0] #Obtendo registro antes de atualizar
        reg_user     = self.user.view_all()
        price        = float(reg[-1]) #Obtendo preço antes de atualizar
        super().update(_id, **kwargs)

        #Atualizando o débito
        if 'user_id' in kwargs:
            #Subtraindo do débito do antigo usuário vinculado a conta
            old_user = [r for r in reg_user if r[0] == reg[1]][0]        
            debt     = float(old_user[2]) - price
            self.user.update(old_user[0], debt=debt)
            #Adicionando ao novo
            new_user = [r for r in reg_user if r[0] == kwargs['user_id']][0]
            debt     = float(new_user[2]) + price
            self.user.update(new_user[0], debt=debt)

        if 'price' in kwargs:
            new_price = float(kwargs['price'])
            new_user = [reg for reg in reg_user if reg[0] == _id][0]
            debt     = float(new_user[2])
            print(debt)
            if price > new_price:
                debt = debt - (price - new_price)
            else:
                debt = debt + (new_price - price)
            self.user.update(new_user[0], debt=debt)


class Records:
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


class User:
    name       = SizedString('name', size=32) 
    debt       = UnsignedFloat('debt') 
    paid_out   = UnsignedFloat('paid_out')  

    def __init__(self, name, debt, paid_out):
        self.name     = name
        self.debt     = debt
        self.paid_out = paid_out