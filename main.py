from console_ui import *
import os 


TITLE = 'GERENCIADOR DE FATURA'

MENU0 = ['USUÁRIO', 'REGISTROS', 'RESUMO DA FATURA', 'SAIR']

MENU1 = {
    'ADICIONAR USUÁRIO': add_user, 
    'REMOVER USUÁRIO': delete_user, 
    'VER USUÁRIOS': view_all_users, 
    'ALTERAR NOME DE USUÁRIO': change_user_name, 
    'ADICIONAR SALDO AO USUÁRIO': increase_balance, 
    'SUBTRAIR SALDO DO USUÁRIO': decrease_balance, 
}

MENU2 = {
    'ADICIONAR REGISTRO': add_register, 
    'REMOVER REGISTRO': delete_register, 
    'VER REGISTROS': view_all_register, 
    'ALTERAR REGISTRO': update_register, 
}

MENUS = [MENU1, MENU2]

if __name__ == '__main__':
    while True:
        os.system('cls')
        op = console_ui(MENU0, TITLE, 'Valor inválido')

        if op == 'SAIR':
            break
        if op == 'RESUMO DA FATURA':
            os.system('cls')
            view_register_summary()
            os.system('pause')
            continue 

        op = MENU0.index(op)
        sub_menu = list(MENUS[op].keys())
        sub_menu.append('VOLTAR')
        op2 = console_ui(sub_menu, MENU0[op], 'Valor inválido')
        if op2 == 'VOLTAR':
            continue
        os.system('cls')
        MENUS[op][op2]()
        os.system('pause')
        