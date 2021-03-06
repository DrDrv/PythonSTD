'''
Спрашиваем у пользователя, какой файл открыть?
Открываем нужный файл.
Выводим в консоль пронумерованное построчно содержимое файла.
Пользователь указывает номер задачи, которую нужно отредактировать.
Возвращаем пользователю нужную строку: название задачи и срок выполнения.
Пользователь вводит новые значения.
Уточняем, будем ли изменять срок выполнения.
При необходимости принимаем новый срок.
Записывем новые данные по индексу в список.
Возвращаем список.
'''
from func import display_all_tasks, save_form_base
from func import save_form
from func import save_form_base
from func import log
import csv

def edit_task(file_now, file_past):
    base_list = display_all_tasks(file_now)
    new_list = list(enumerate(base_list))
    what_is_task = int(input("Введите номер задачи: "))
    what_is_ready = str(input("Задача завершена? (y/n): \t"))
    
    
    if what_is_ready == 'y':
        save_form(base_list[what_is_task],file_past)
        log(f'Запись {base_list[what_is_task]} перемещена в выполненные')

        base_list.pop(what_is_task)
        
        save_form_base(base_list,file_now)


        return

    edit_line = ((new_list[what_is_task])[1]).split(';')
    edit_line[0] = input(f"Измените текст задачи {edit_line[0]}: \t")
    edit_line[1] = input(f"Введите новый срок выполнения задачи {edit_line[1]}: \t")   
    edit_line = edit_line[0] + ';' + edit_line[1]
    base_list[what_is_task] = edit_line
    
    save_form_base(base_list,file_now)
    log(f'Запись {base_list[what_is_task]} изменена')
    return
