from InvoiceManager import *


register = RegisterManager()
user     = UserManager()

#user.save(name='Matheus', debt=.0, paid_out=.0)
#user.delete(_id=1)
#register.save(user_id=1, date='22/04/2001', purchase_id='teste', installments='05/10', price=100.0)
#register.delete(1)
register.update(1, **{})
print(register.view_all())
print(user.view_all())
