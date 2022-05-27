# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
print('---= Задача 1 =---')
import random
num = 10
def generator_list(N):
    gen_list = []
    for i in range(0,N):
        gen_list.append(random.randint(-N,N))
    return gen_list

def generator_file(N):
    with open('file_pyt3.txt','w') as file:
        for i in range(N):
            file.write(str(random.randint(0,N-1)) + '\n')

def multi_index(N, values):
    mult_i = 1
    with open('file_pyt3.txt','r') as file:
        for i in file:
            mult_i *= values[int(i)]
    return mult_i

list_values = generator_list(num)
print(list_values)
generator_file(num)
print(multi_index(num,list_values))


"""
Пример вывода программы:
---= Задача 1 =---
[2, 0, 10, -7, -9, -7, 1, 5, -3, 1]
-113400

значения в файле:
7
0
4
0
7
0
9
5
4
9
"""

# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
print('---= Задача 2 =---')
def fibb(n):
    if n in [0]:
        return 0
    elif n in [1,2,-1]:
        return 1
    elif n in [-2]:
        return -1
    elif n > 2:
        return fibb(n-1) + fibb(n-2)
    elif n < -2:
        return fibb(n+2) - fibb(n+1) 

list = []
k = 8
for e in range (-k, k+1):
    list.append(fibb(e))
print(list)

"""
Вывод программы
---= Задача 2 =---
[-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
print('---= Задача 3 =---')
print(list_values)

def find_min_max(f_list):
    length_list = len(f_list)
    min, max = f_list[0], f_list[0]
    for k in f_list:
        if k < min: min = k
        if k > max: max = k
    return [min, max]


print(f'Минимум и максимум списка: {find_min_max(list_values)}')
"""
Вывод программы:
---= Задача 3 =---
[-7, 1, -3, 9, 2, 4, -6, -5, -5, -4]
Минимум и максимум списка: [-7, 9]
"""