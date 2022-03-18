import os


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
