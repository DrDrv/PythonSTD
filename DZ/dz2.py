# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

print('---= Задача 1 =---')
text_list = [1,2,3,4,5] # Входные данные

def sum_from_oddindex(t_list):        # На вход - список
    lenght_list = len(t_list)          # Количество элементов списка
    rezult_summ = 0                     # Сумма искомых элементов
    for i in range(0,lenght_list,2):
        rezult_summ += t_list[i]
    return rezult_summ
    
print(f'Сумма чисел списка {text_list} стоящих на нечетной позиции - {sum_from_oddindex(text_list)}')

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
print('---= Задача 2 =---')
digit_list = [2, 3, 4, 5, 6]    # Входной список

def multi_para(d_list):
    kol_par = len(d_list)//2+len(d_list)%2 # Количество пар для произведение
    n_list = []     # новый список для вывода результата
    for i in range(0,kol_par):
        n_list.append(d_list[i] * d_list[-(i+1)])
    return n_list

print(f' Входной список - {digit_list}')
print(f' Выходной список - {multi_para(digit_list)}')

# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('---= Задача 3 =---')
float_list = [1.1, 1.2, 3.1, 5, 10.01]    # Входной список

def compare_para(d_list):
    lenght_list = len(d_list)          # Количество элементов списка
    for i in range(0,len(d_list)):
        if d_list[i]%1 != 0: 
            d_list[i] = float( '0.' + (str(d_list[i]).split('.'))[1]) 
            if i == 0:
                max = d_list[i]
                min = d_list[i]
            if max < d_list[i]:
                max = d_list[i]
            if min > d_list[i]:
                min = d_list[i]    
    return [max-min]

print(f' Входной список - {float_list}')
print(f' Результат - {compare_para(float_list)}')

# Написать программу преобразования десятичного числа в двоичное
print('---= Задача 4 =---')
def dec_to_bin(dec):        # На вход - десятичное число
    print(f'Десятичное число - {dec}')
    bin = ''        # Двоичное число в строке, что б потом не переворачивать
    while dec >= 2:
        bin = str(dec - (dec//2)*2) + bin
        dec //= 2
    if dec < 2 : bin = str(dec) + bin 
    return bin
    
print(f'Двоичное число - {dec_to_bin(10)}')


# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.

# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:

# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена. Следите за количеством догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.

# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
# 5.2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.Какое самое маленькое число делится нацело на все числа от 1 до 20?