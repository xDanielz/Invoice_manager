from sqlite3dbmanager.DataBaseManager import DataBaseManager
from tables import User, Register


userdbman     = DataBaseManager('INVOICE', 'user')
registerdbman = DataBaseManager('INVOICE', 'register')

user = User('Daniel', .0, .0)
register = Register(1, '22/04/2001', 'xbox', '06/10', 249.90)

print(registerdbman.view(price=249.90))