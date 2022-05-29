# 1. Найти НОК двух чисел
print('---= Задача 1 =---')
number_a = 111    # Входные данные
number_b = 12

def multi_nok(na, nb):
    mn = min(na,nb)
    if mn == 0: return ('Не существует')
    mn = max(na,nb)
    while True:
        if mn%na == 0 and mn%nb == 0:
            return mn
        mn += 1

print(f'Для чисел {number_a} и {number_b} НОК  =  {multi_nok(number_a, number_b)}')

#Вычислить число  c заданной точностью d
#     Пример: при d = 0.001,  c= 3.141.

print('---= Задача 2 =---')
def number_pi(delta):   # дельта это точность
    num_cols = 1 # Номер члена послесдовательности расчета числа Пи
    num_pi = 0  # Число Пи
    element = 1 # значение элемента последовательности
    while element >= delta:
        element = 1/(2*num_cols -1)
        if num_cols%2 == 0: num_pi -= element
        else: num_pi += element
        num_cols += 1
    num_pi *= 4
    return (num_pi)

print(number_pi(0.001))

# Составить список простых множителей натурального числа N
print('---= Задача 3 =---')
number_N = 12
print(f'простые множители для числа {number_N}')

def simple_mult(N):
    if N in [2,3,5,7]:
        return N
    if N%2 != 0 and N%3 != 0 and N%5 != 0 and N%7 != 0:
        if (pow(N,1/2))%1 == 0: return simple_mult(int(pow(N,1/2)))
        return N
    if N%2 == 0: return simple_mult(N/2)
    if N%3 == 0: return simple_mult(N/3)
    if N%5 == 0: return simple_mult(N/5)
    if N%7 == 0: return simple_mult(N/7)

list = []
while number_N != 1:
    funk_rez = int(simple_mult(number_N))
    list.append(funk_rez)
    number_N = (number_N/funk_rez)
print(list)

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
print('---= Задача 4 =---')
list_in = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'Входящий список {list_in}')
i = len(list_in)-1          # Длина входящего списка
while i >= 0:
    if list_in.count(list_in[i]) > 1:
        list_in.pop(i)
    i -= 1
print(f' Результат {list_in}')

# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
print('---= Задача 5 =---')
import random
def int_number_list(file_in):
    N = 10                                  # Число целых цифр
    with open(file_in,'w') as file:
        for i in range(N):                  
            file.write(str(random.randint(0,N-1)) + '\n')
    print('содержимое входящего файла: ')
    with open(file_in,'r') as file:
        for i in file:
            print(str(int(i))+' ')     
    return

def del_krat_two(file_in):
    collection_nechet = []          # список для промежуточного хранения данных
    with open(file_in,'r') as file:
        for i in file:
            if int(i)%2 != 0: collection_nechet.append(str(i))
    with open(file_in,'w') as file:
        print('содержимое выходного файла: ')
        for i in collection_nechet:
            print(str(int(i))+' ')
            file.write(str(i))
    return

int_number_list('file_dz3.txt')
del_krat_two('file_dz3.txt')