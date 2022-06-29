def menu_interface():
    from termcolor import colored
    
    list_menu = ['1. Добавить контакт', '2. Редактировать контакт', '3. Импорт/Экспорт', '4. Выход']
    menu = '|'
    for i in list_menu: menu += ' '+ colored(f'{i}','green') + ' |'
    print(f'{menu}')