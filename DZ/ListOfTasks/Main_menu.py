def menu():
    def menu_interface():
        list_menu = ['1. Добавить запись     ', '2. Список текущих дел', '3. Редактировать запись', '4. Посмотреть завершенные', '5. Выход             ']
        len_id_menu = len(list_menu[0])
        for i in list_menu:
            if len_id_menu < len(i):
                len_id_menu = len(i)
        len_id_menu += 9
        print('\t Задачник \t')
        print('='*len_id_menu)
        for i in list_menu:
            print(f'+  {i} \t +')
        print('='*len_id_menu)
        print('')
        return list_menu
    
    res = 0
    while res != -1:
        l_menu = menu_interface()
        id_menu = 0
        id_menu = input(f'Выберите пункт меню (1-{len(l_menu)}): ')
        if id_menu.isdigit():                                                   # Проверка на цифры
            if int(id_menu) > 0 and int(id_menu) < len(l_menu)+1: res = -1      # Проверка на диапазон пунктов

    return id_menu