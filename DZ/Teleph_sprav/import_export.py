def impexp_file(list_in):
    from adr_func import show, add_persons, csv_to_list
    import os.path
    from termcolor import colored

    print('Импорт/Экспорт файла контактов')
    file_exist = False
    while file_exist != True:
        print(colored('| 1. Импорт | 2. Экспорт | 3. Выход','green'))
        in_put = input(colored('Выберите действие: ','blue'))
        if in_put == '3': return # Выход из модуля
        # Раздел обработки импорта файла
        if in_put == '1':
            import_file = input(f'Введите имя файла для импорта: ')
            file_exist = os.path.exists(import_file)  # Проверка на существование файла
            if file_exist == True: 
                print(colored(f'{import_file} - файл найден...','green'))
                print('Чтение файла')                              # - Удалить при слиянии
                import_list = csv_to_list(import_file)    # Получаем данные из файла
                show(4, import_file)                        # Показать пользователю импортированные данные
                y_n = input(colored(f'Выполнить импорт? (y/n): ','blue'))
                if y_n == 'y': 
                    list_in += import_list
                    add_persons(list_in,'')  # Записываем данные в файл (если '' - то файл по умолчанию, иначе указанный файл)
            elif file_exist == False: print('Файл отсутствует!') # Возврат в меню модуля
        
        # Раздел обработки экспорта в файл
        if in_put == '2':
            export_file = input(f'Введите имя файла для экспорта: ')
            file_exist = os.path.exists(export_file)  # Проверка на существование файла
            if file_exist == True: 
                print(colored(f'{export_file} - файл существует! Перезаписать? (y/n): ','red'))
                if y_n == 'y': 
                    add_persons(list_in, export_file)  # # Записываем данные вуказанный  файл (если ' - то файл по умолчанию)
            elif file_exist == False:
                file_exist = True
                add_persons(list_in, export_file)  # # Записываем данные вуказанный  файл (если '' - то файл по умолчанию)
