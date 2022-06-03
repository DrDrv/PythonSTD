# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
list_in = [1, 5, 2, 3, 4, 6, 1, 7]
print(f'Входящий лист - {list_in}')
def split_list(li):
    lo = []
    length_li = len(li)
    for k in range(0,length_li):
        max = int(li[k])
        loi = []
        loi.append(str(li[k]))
        for i in range(k,length_li):            # Прогоняем слева на право если предыдущий меньше следующего - забираем  
            if int(li[i]) > max:
                loi.append(str(li[i]))
                max = li[i]
        if len(loi) > 1: 
            lo.append(loi)
            a=loi
        min = int(li[-k])
        loi = []
        loi.append(str(li[-k]))
        for i in range(length_li-1-k,-1,-1):        # Прогоняем справа на лево если предыдущий Больше следующего - забираем 
            if li[i] < min:
                loi.insert(0,str(li[i]))
                min = li[i]
        if len(loi) > 1: 
            lo.append(loi)
            b = loi
        if k > 0 and k < length_li-1 and li[k-1] < li[k] and li[k] < li[k+1]:           # Проверяем лево и право и сливаем, что бы не упустить последовательности
            loi = a+b
            z = len(loi)-1
            while z >= 0:
                if loi.count(loi[z]) > 1:
                    loi.pop(z)
                z -= 1
            loi.sort()
            lo.append(loi)
    return lo
rezultat = split_list(list_in)
print(f'Возрастающие последовательности {rezultat}')            # Вернули все найденные последовательности в список



# Задача 3
max_len = len(rezultat[0])          # Находим максимальную по длине возврастающую последовательность
for i in rezultat:
    
    if max_len < len(i):
        max_len = len(i)
        rez = i 
print(f'Масимальная по длине возрастающая последовательность {rez}')

# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

import random

filename = 'file_dz4.txt'

# ВВод первоначальных данных - И запись в файл 
in_list = []
for i in range(20):                  
    in_list.append(random.randint(1,50))
print(in_list)

with open(filename,'w') as f:
    f.write("\n".join(map(str,in_list)))

# Из предыдущего ДЗ - я не понимаю - делаем чтение файла или работаем со списком???? 
def bubble_sort(lst):          # Сортировка пузырком - ничего нового 
    
    #swapped = False
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(bubble_sort(in_list))
