import os
from prettytable import PrettyTable


class UserInterface:
    def __init__(self, dbmanager, columns):
        self.dbmanager = dbmanager
        self.columns = dict(columns)
    
    def save(self, title=None):
        reg = {}

        while True:
            os.system('cls')
            
            if title is not None:
                print(title+'\n')

            for k, v in self.columns.items():
                value  = input(f'{k}: ')
                reg[v] = value

            try:
                self.dbmanager.save(**reg)

            except Exception as e:
                print(f'\nAlgo deu errado:\n{e}')

            else:
                print(f'\nOperação {title} Realizada com Sucesso!')
                os.system('pause')

            while True:
                op = input('\nContinuar? [S/N]: ')
                if op in 'S s N n'.split():
                    break
            if op in 'Nn':
                break 


    def update(self, title=None):
        reg = {}
        
        while True:
            os.system('cls')

            if title is not None:
                print(title+'\n')

            print('(Deixe em branco o que não deve ser alterado)')
            
            try:
                _id      = input('ID: ')
                register = self.dbmanager.view(id=_id)[0]

                for k, v in zip(self.columns, register[1:]):
                    value = input(f'{k} [{v}]: ')
                    if value:
                        reg[self.columns[k]] = value

                if reg:
                    self.dbmanager.update(_id, **reg)
                
            except Exception as e:
                print(e)

            else:
                print(f'\nOperação {title} Realizada com Sucesso!')
                os.system('pause')

            while True:
                op = input('\nContinuar? [S/N]: ')
                if op in 'S s N n'.split():
                    break
            if op in 'Nn':
                break

    
    def view(self, title=None):
        filter = {}
        columns = ['Id']
        columns.extend(self.columns)
        pt = PrettyTable(columns)

        op = console_ui(['TODOS', 'FILTRAR'], 'EXIBIR', 'Opção inválida')
        if not op:
            rows = self.dbmanager.view_all()

        else:
            while True:
                os.system('cls')

                if title is not None:
                    print(title+'\n')

                for attr in self.columns:
                    value = input(f'{attr}: ')
                    if value:
                        filter[self.columns[attr]] = value
                    
                try:
                    rows = self.dbmanager.view(**filter)

                except Exception as e:
                    print(e)

                while True:
                    op = input('\nContinuar? [S/N]: ')
                    if op in 'S s N n'.split():
                        break
                if op in 'Nn':
                    break
        
        pt.add_rows(rows)
        print(pt)
        total = sum([value[-1] for value in rows])
        print(f'\nTOTAL: {total:.2f}\n')
        os.system('pause')

    def delete(self, title=None):
        while True:
            os.system('cls')
            
            if title is not None:
                print(title+'\n')

            try:
                _id = input('ID: ')
                self.dbmanager.delete(_id)

            except Exception as e:
                print(e)

            else:
                print(f'Operação {title} Realizada com Sucesso!')
                os.system('pause')

            while True:
                op = input('\nContinuar? [S/N]: ')[0]
                if op in 'SsNn':
                    break
            if op in 'Nn':
                break
    

            
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

        return option - 1
    
