from InvoiceManager import *
from consoleui import *

register = RegisterManager()
user     = UserManager()

user_ui = UserInterface(user, {
    'Nome'  : 'name', 
    'Débito': 'debt', 
    'Pagou' : 'paid_out'
    })

register_ui = UserInterface(register, {
    'ID de Usuário'          : 'user_id', 
    'Data'                   : 'date', 
    'Identificação de Compra': 'purchase_id', 
    'Parcelas'               : 'installments', 
    'Valor'                  : 'price'
    })

if __name__ == '__main__':
    while True:
        tables = [register_ui, user_ui]
        error_msg = 'Opção inválida'
        menu1 = (['REGISTROS', 'USUÁRIOS', 'SAIR'], 'GERENCIADOR DE FATURA', error_msg)
        op1 = console_ui(*menu1)

        if op1 == len(menu1[0]) - 1:
            break 

        table = tables[op1]
        methods = [table.save, table.delete, table.update, table.view]
        menu2 = (['ADICIONAR', 'REMOVER', 'ALTERAR', 'EXIBIR', 'VOLTAR'], menu1[0][op1], error_msg)
        op2 = console_ui(*menu2)

        if op2 == len(menu2[0]) - 1:
            continue

        methods[op2](f'{menu2[0][op2]} {menu1[0][op1]}')
