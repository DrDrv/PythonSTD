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
def number_pi(delta):
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
number_N = 26
print(f'простые множители для числа {number_N}')

def simple_mult(N):
    if N in [2,3,5,7]:
        return N
    if N%2 != 0 and N%3 and N%5 != 0 and N%7 != 0:
        if (pow(N,1/2))%1 == 0:
            print(pow(N,1/2))
            return simple_mult(int(pow(N,1/2)))
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



