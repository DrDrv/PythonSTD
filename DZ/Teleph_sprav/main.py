from adr_func import show, add_person, add_persons, csv_to_list
from import_export import impexp_file
from edit import edit_contact
from menu import menu_interface
from termcolor import colored
import os

id_menu = 0 
while id_menu != '4':
    clear = lambda: os.system('cls')
    clear()
    show(4,'')
    menu_interface()
    id_menu = input(colored(f'Select an action: ','blue'))
    if id_menu == '4': break
    if id_menu == '3': 
        show(4,'')
        impexp_file(csv_to_list(''))
    if id_menu == '2': 
        show(4,'')
        add_persons(edit_contact(csv_to_list('')),'')
    if id_menu == '1': 
        add_person()