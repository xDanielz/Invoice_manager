from InvoiceDbManager import User as _user
from InvoiceDbManager import Register as _register
from verification_tools import *
from prettytable import PrettyTable
import os


def add_register():
    while True:
        print('ADICIONAR REGISTRO\n')
        user_id      = verification(lambda num: num.isnumeric(), 'ID de Usuário: ', 'Valor inválido')
        date         = verification(date_verification, 'Data: ', 'Formato de data inválido')
        installments = verification(installments_verification, 'Parcelas: ', 'Formato de parcela inválido')
        purchase_id  = input('Identificação de compra: ')
        price        = verification(isdecimal, 'Preço: ', 'Valor inválido')
        answer = proceed('S s N n'.split(), 'ADICIONAR NOVO REGISTRO ?[S|N]: ')
        if answer in 'Ss':
            try:
                _register.save(user_id, date, purchase_id, installments, price)
            except Exception as e:
                print(f'\nAlgo deu errado:\n{e}')
            else:
                print('\nOperação realizada com sucesso!')
        answer = proceed('S s N n'.split(), 'ADICIONAR MAIS REGISTROS ?[S|N]')
        if answer in 'Nn':
            break
        else:
            os.system('cls') 
     
def add_user():
    print('ADICIONAR USUÁRIO\n')
    name = input('Nome: ')
    name = name.upper()
    answer = proceed('S s N n'.split(), f'ADICIONAR USUÁRIO {name}?[S|N]: ')
    if answer in 'Ss':
        try:
            _user.save(name)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!') 

def update_register():
    print('ATUALIZAR REGISTRO\n')
    _id = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido')
    reg = _register.filtered_view(_id=_id)[0]
    
    kwargs = {
        'UserID'       : verification(canblank(lambda num: num.isnumeric()), f'ID de Usuário[{reg[1]}]: ', 'Valor inválido'),
        'Date'         : verification(canblank(date_verification), f'Data[{reg[2]}]: ', 'Formato de data inválido'),
        'PurchaseID'   : input(f'Identificação de compra[{reg[3]}]: '),
        'Installments' : verification(canblank(installments_verification), f'Parcelas[{reg[4]}]: ', 'Formato de parcela inválido'),
        'Price'        : verification(canblank(isdecimal), f'Preço[{reg[5]}]: ', 'Valor inválido')
    }

    kwargs = {k: v for k, v in kwargs.items() if v != ''}
    answer = proceed('S s N n'.split(), f'SALVAR NOVO REGISTRO ?[S|N]: ')
    if answer in 'Ss':
        try:
            _register.update(_id, **kwargs)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!')
            

def change_user_name():
    print('ALTERAR NOME DE USUÁRIO\n')
    _id = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido')
    name = input('Novo Nome: ').upper()
    answer = proceed('S s N n'.split(), f'ALTERAR NOME DO USUÁRIO {_id} ?[S|N]: ')
    if answer in 'Ss':
        try:
            _user.change_name(_id, name)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!')


def increase_balance():
    print('ADICIONAR SALDO AO USUÁRIO\n')
    _id   = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido') 
    price = verification(isdecimal, 'Valor: ', 'Valor inválido')
    answer = proceed('S s N n'.split(), f'INCREMENTAR USUÁRIO {_id} ?[S|N]: ')
    if answer in 'Ss':
        try:
            _user.increase_balance(_id, price)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!')

def decrease_balance():
    print('SUBTRAIR SALDO DO USUÁRIO\n')
    _id   = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido') 
    price = verification(isdecimal, 'Valor: ', 'Valor inválido')
    answer = proceed('S s N n'.split(), f'DECREMENTAR USUÁRIO {_id} ?[S|N]: ')
    if answer in 'Ss': 
        try:
            _user.decrease_balance(_id, price)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!')

def delete_user():
    print('REMOVER USUÁRIO\n')
    _id   = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido')
    answer = proceed('S s N n'.split(), f'DELETAR USUÁRIO {_id} ?[S|N]: ')
    if answer in 'Ss':
        try:
            _user.delete(_id)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!') 

def delete_register():
    print('REMOVER REGISTRO\n')
    _id   = verification(lambda num: num.isnumeric(), 'ID: ', 'Valor inválido')
    answer = proceed('S s N n'.split(), f'DELETAR REGISTRO {_id} ?[S|N]: ')
    if answer in 'Ss':
        try:
            _register.delete(_id)
        except Exception as e:
            print(f'\nAlgo deu errado:\n{e}')
        else:
            print('\nOperação realizada com sucesso!')  

def view_all_register():
    print('REGISTROS\n')
    pt = PrettyTable(['ID', 'NOME', 'DATA', 'COMPRA_ID', 'PARCELAS', 'VALOR'])
    pt.add_rows(_register.view_all())
    print(pt) 

def view_register_summary():
    print('RESUMO\n')
    pt = PrettyTable(['NOME', 'DEVE', 'PASSOU'])
    pt.add_rows(_register.view_register_summary())
    print(pt)

def view_all_users():
    print('USUÁRIOS\n')
    pt = PrettyTable(['ID', 'NOME', 'SALDO'])
    pt.add_rows(_user.view_users())
    print(pt)

def view_user():
    print('REGISTROS\n')
    name = input('Informe o nome do usuário: ').upper()
    pt = PrettyTable(['ID', 'DATA', 'COMPRA_ID', 'PARCELAS', 'VALOR'])
    rows = _register.filtered_view(name=name)
    pt.add_rows(rows)
    print(pt)

def console_ui(menu_list: list, title: str, error_msg: str) -> int:
    while True:
        os.system('cls')
        menu_list = tuple(menu_list)
        print(str(title).upper()+'\n')

        for i, o in enumerate(menu_list, 1):
            print(f'{i} - {o}')

        option = input(': ')

        try:
            option = int(option)
            assert option in range(1, len(menu_list)+1)
        except:
            print(error_msg)
            os.system('pause')
            continue

        return menu_list[option-1]