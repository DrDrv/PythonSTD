from ast import match_case
from Main_menu import menu
from func import add_task
from func import display_all_tasks
from edit_task import edit_task
import os.path


files = ['list_of_tasks.csv','list_of_oldtasks.csv','log.txt']
for i in files:
    file_exist = os.path.exists(i)
    if file_exist == False:
        with open(i, 'w') as file:
             file.write('')

id_menu = 0
while id_menu != '5': 
    id_menu = menu()
    match id_menu:
        case '1': add_task()
        case '2': 
            print('++++++++++++++++++++++++++')
            print('Список ваших текущих задач')
            print('++++++++++++++++++++++++++')
            display_all_tasks('list_of_tasks.csv')
            print('++++++++++++++++++++++++++')
        case '3':
            print('++++++++++++++++++++++++++')
            print('Редактирование записи')
            print('++++++++++++++++++++++++++')
            edit_task('list_of_tasks.csv','list_of_oldtasks.csv')
        case '4': 
            print('++++++++++++++++++++++++++')
            print('Список ваших завершенных задач')
            print('++++++++++++++++++++++++++')
            display_all_tasks('list_of_oldtasks.csv')
            print('++++++++++++++++++++++++++')
        case '5': break

