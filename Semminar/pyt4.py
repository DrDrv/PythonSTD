# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n. 
# *Пример: n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# n=3 => 5*x**3 + 17*x**2 =0

import random

n = 10 # степень уравнения

def print_qual(N):
    list = []
    for i in range(0, N+1):
        list.append(random.randint(0,50))
    len_list = len(list)
    formula = ''
    step = N
    if list[0] == 0: return "first element is 0"
    if step == 0 or step == 1: return "non equalent"
    for i in range(0, len_list):
        if list[i] != 0: 
            if i == len_list-2: 
                list[i] = str(list[i]) + 'x'
            elif i == len_list-1: 
                list[i] = str(list[i]) + ' = 0'
            else: 
                list[i] = str(list[i]) + "x**" + str(step) + ' + '
            formula += list[i]    
        if i == len_list-1 and list[i] == 0 : 
            list[i] = ' = 0'
            formula = formula[:-2]
            formula += list[i]
        step -= 1
    return formula

with open('file_pyt4.txt','w') as file:
    file.write(print_qual(n))