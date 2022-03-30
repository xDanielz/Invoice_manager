import os
from prettytable import PrettyTable


class UserInterface:
    def __init__(self, dbmanager, **columns):
        self.dbmanager = dbmanager
        self.columns = list(columns)
    
    def save(self):
        reg = {}
        while True:
            for attr in self.columns:
                reg[self.columns[attr]] = input(f'{attr}: ')
            try:
                self.dbmanager.save(**reg)
            except Exception as e:
                print(e)
                os.system('pause')
                os.system('cls')
                continue
            break

    def update(self):
        reg = {}
        while True:
            print('(Deixe em branco o que não deve ser alterado)')
            try:
                _id = input('ID: ')
                register = self.dbmanager.view(_id=_id)[0]

                for k, v in zip(self.columns, register):
                    value = input(f'{k} [{v}]: ')
                    if value:
                        continue
                    reg[self.columns[k]] = value

                if reg:
                    self.dbmanager.update(_id, **reg)
                
            except Exception as e:
                print(e)
                os.system('pause')
                os.system('cls')
                continue
            break
    

    def delete(self):
        while True:
            try:
                _id = input('ID: ')
                self.dbmanager.delete(_id)
            except Exception as e:
                print(e)
                os.system('pause')
                os.system('cls')
                continue
            break
    
    def view(self):
        filter = {}
        pt = PrettyTable(self.columns.keys())
        while True:
            for attr in self.columns:
                value = input(f'{attr}: ')
                if value:
                    continue
                filter[self.columns[attr]] = value
            
            try:
                if filter:
                    rows = self.dbmanager.view(**filter)
                else:
                    rows = self.dbmanager.view_all()
                pt.add_rows(rows)

            except Exception as e:
                print(e)
                os.system('pause')
                os.system('cls')
                continue

            print(pt)
            os.system('pause')
            break

            
def console_ui(menu_list, title, error_msg):
    os.system('cls')
    menu_list = tuple(menu_list)
    print(str(title).upper()+'\n')

    for i, o in enumerate(menu_list, 1):
        print(f'{i} - {o}')

    option = input(': ')

    try:
        option = int(option)
        assert option in range(1, len(menu_list)+1)
    except (ValueError, AssertionError):
        print(error_msg)
        os.system('pause')
        console_ui(menu_list, title, error_msg)

    return option
