# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
print(f"+++- Задача 1 -+++")
def swing(N):
    rezultat = []
    for i in range(0,N):
        rezultat.append((-3)**i)
    return(rezultat)

print(swing(5))

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
print(f"+++- Задача 2 -+++")
def findtext(element,text):
    count = 0   # счетчик вхождений
    i = 0       # счетчик элементов для цикла
    len_text = len(text)     # Длина строки текста поиска
    len_element = len(element)       # длина искомой строки
    while i < (len_text-len_element+1):
        if element == text[i:i+len_element]:
            count += 1
            i = i + len_element
            print(f"        Номер элемента вхождения в искомом тексте - {i}")
        else: i += 1
    return count

print(f"Число вхождений - {findtext('11','4w95793094509234111117656757616717657657611')}")

# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
#  [ 1, 2, 6, 24 ]
print(f"+++- Задача 3 -+++")

def multirow(N):
    print(f"Входящее число N = {N}")
    array = [0 for i in range(N)]
    for k in range(0,N):
        if k == 0: 
            array[k] = 1
        else:
            array[k] = array[k-1]*(k+1)
    return array

print(multirow(4))

# Подсчитать сумму цифр в вещественном числе.
print(f"+++- Задача 4 -+++")

def summelements(V):
    print(f"Входящее число V = {V}")
    summel = 0
    for i in str(V):
        if i.isdigit():
            summel += int(i)
    return summel

print(f"Сумма всех числе входящего вещественного числа = {summelements(23.141)}")