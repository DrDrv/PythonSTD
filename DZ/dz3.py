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

n = 5
a = 1.2345678912345
template = '{:.' + str(n) + 'f}'
print(template.format(a))