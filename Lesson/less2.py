# # Работа с файлами
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+ - Записывать и добавлять
# r+ - Читать и добавлять

"""
colors = ['red', 'green', 'blue']
file_data = open('file_less2.txt', 'w')
file_data.writelines(colors) # пишем без раздилителей
file_data.write('\n')    # перенос строки
file_data.write('new line')
file_data.close()

path = 'file_less2.txt'
data = open (path, 'r')
for line in data:
    print(line)
data.close()

with open('file_less2.txt','r') as fil:
    for line in fil:
        print(line)
"""
"""
# Функции и модули
import less1 as h

print(h.f())

# передача неограниченного количества аргументов
def primer(*params):
    res: str = ''
    for item in params:
        res += item
    return res
print(primer('a','s','d','4','6','v','h'))
"""
# РЕКУРСИЯ

def fibb(n):
    if n in [1,2]:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

list = []
for e in range (1, 10):
    list.append(fibb(e))
print(list)

# Кортежи - не изменяемый список

a = (1, 2)
print(a)
print(type(a))

# Словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу
dict = {}
dict = \
    {
        # keys   # values
        'up': '1',
        'down': '2'
    }
print(dict['up'])   # 1

# Множества
colors = {'red', 'green', 'blue'}
print(colors)
print(type(colors))
# add
# remove  - если удалить не существующее, то ошибка
# diskard - удалить если существует?
# clear

a = colors.copy()

# a, b - множества
# Объединение множеств union   a.union(b)
# Пересечение a.intersection(b)
# исключение a.difference(b)

s = frozenset(a) # Заморозка множества a в переменной s

print(s)

# Списки
# list.pop - удаление элемента по индексу
# list.index - добавление элемента по индексу