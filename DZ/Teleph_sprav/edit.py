def edit_contact(contacts: list) -> list:
    from termcolor import colored
    """Редактирование контакта
    если введено не число -> ошибка ввода -> list
    если контакт не найден -> контакт не найден -> list
    :return: list
    """
    if not contacts:
        print(colored('Список контактов пуст!','red'))
        return contacts
    try:
        id_cont = int(input(colored('Номер контакта для редактирования: ', 'blue')))
    except ValueError:
        print(colored('Ошибка ввода','red'))
        return contacts
    tmp = ""
    no_contact = True
    # Удаление контакта
    y_n = input(colored(f'Удалить контакт? (y/n): ','blue'))
    if y_n == 'y':
        contacts.pop(id_cont)
        return contacts 
    # 
    for key, value in enumerate(contacts):
        if id_cont == key:
            no_contact = False
            for i in range(len(value)):
                tmp = value[i]
                value[i] = input(f"Старое значение {colored(f'{value[i]:15}', 'green')},"
                                 f" введите новое "
                                 f"{colored('(Enter=оставить как есть): ', 'yellow')}").strip()
                if value[i] == '':
                    value[i] = tmp
    if no_contact:
        print("Нет такого контакта")
        return contacts
    return contacts
