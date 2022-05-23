
# Реализовать алгоритм задания случайного числа без генератора случайных чисел
print(f"+++- Задача 1 -+++")
from datetime import datetime
def randomize(min,max):
    rand = int(((datetime.now()).microsecond)%100)
    #print(rand)
    rand = min + rand*(max-min)//100
    return (rand)

print(randomize(0,20))

# Реализуйте алгоритм перемешивания списка.
print(f"+++- Задача 2 -+++")
def random_sort(list):
    len_list = len(list)
    new_list = []
    for i in range(len_list):
        new_list.append(list[randomize(0,len_list)])
        list.remove(new_list[i])
        len_list -= 1
    return new_list

in_list = [12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f" Входной массив - {in_list}")
print(f" Выходной массив - {random_sort(in_list)}")

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
print(f"+++- Задача 3 -+++")
def swing(N):
    rezultat = []
    summ = 0
    for i in range(1,N+1):
        rezultat.append((1+1/i)**i)
        summ += rezultat[i-1]
    print(f"Заданный список из N элементов - {rezultat}")
    return(summ)

print(f"Сумма значений из списка = {swing(8)}")

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
# ['geek', 'brains4', '5five', 3friends']
print(f"+++- Задача 4 -+++")
mass_text = ['geek', 'brains4', '5five', '3friends']
def find_digital(N, list):
    for i in list:
        for k in i:
            if (k.isdigit()) and (int(k) == N):  
                return ("есть")  
    return ("отсутствует")

print(f"Искомое число в массиве {find_digital(3 , mass_text)}")