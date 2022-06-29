import csv
import datetime
import datetime
from view import presentations




def display_all_tasks(file_task):
    """
    :return: Ничего не возвращает, а просто печатает все строчки из list_of_tasks.csv .
    """
    with open(file_task, 'r') as file:
        reader = list(csv.reader(file))

    return presentations(reader)



def add_task():
    """
    :return: При запуске запрашивает у пользователя Задачу и дату выполнения (в формате YYYY-MM-DD)
    затем записывает это в файл 'list_of_tasks.csv' без \n с разделителем ; 
    """
    import datetime
    task = input('Введите задачу: ')
    date_entry = input('Введите дату deadline в формате YYYY-MM-DD: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    with open('list_of_tasks.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([task, f'{date1}'])
    log(f'Запись {task} создана')

def save_form(lst_data, file):
    with open(file, 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        task = lst_data.split(';')
        writer.writerow([task[0], f'{task[1]}'])
    return

def save_form_base(lst_data, file):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for i in lst_data:
            task = str(i).split(';')
            writer.writerow([task[0], task[1]])
    return
        
    import datetime


def log(what_happening: str):
    with open('log.txt', 'a+') as file:
        file.write(f'{datetime.datetime.now()}-----{what_happening} \n')
    return
