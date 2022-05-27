# 1. Найти НОК двух чисел

number_a = 12    # Входные данные
number_b = 45

def multi_nok(na, nb):
    min = na
    if na>nb: min = nb
    while True:
        if min%na == 0 and min%nb == 0:
            return min
        min += 1

print(multi_nok(number_a, number_b))

