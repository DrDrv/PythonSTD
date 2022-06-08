"""
# 1. Напишите программу, удаляющую из текста все слова содержащие "абв". Используйте знания с последней лекции. Выполните ее в виде функции. 
"""
# print(' ================================')
# print('Удаление фрагмента текста')
# print('')
# from gettext import find

# in_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
# text = 'абв'
# print(f'Исходная строка: \t {in_text}')
# print(f'Искомый текст: \t\t {text}')

# def nega_text(in_t, txt):
#     data = list(map(str,in_t.split()))
#     data = [i for i in data if (i.lower()).find(txt) == -1]
#     data = ' '.join(data)
#     return data

# print(f'Результат: \t\t {nega_text(in_text,text)}')

"""
# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 
"""

# print(' ================================')
# print('Крестики - нолики')
# print('')

# pole = '*********'                                  # Поле - 9 ячеек, хотел списком, но мороки с проверкой много
# step = 1                                            # Ходы - разделяем игроков по чет/нечет
# sign = ''                                           # Символ X/O

# def vision_pole(pole):                              # Функция отобрвжения поля
#     for k in range(0,3):
#         str_pole = ''
#         for i in range(0,3):
#             if pole[k*3+i] == '*': str_pole += str(k*3+i+1)
#             if pole[k*3+i] != '*': str_pole += pole[k*3+i]
#             if i < 2: str_pole += ' | '
#         print(str_pole)
#         print('----------')

# def check_win(st):
#     win_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    #Выигрышные комбинации
#     return [l for l in win_comb if pole[l[0]] == st and pole[l[1]] == st and pole[l[2]] == st]

# vision_pole(pole)
# res = 0
# while res != -1:
#     if step%2 == 0: sign = 'O'
#     else: sign = 'X'
#     a = input(f'Ход {step} для {sign}, выберите поле: ')
#     if a.isdigit():
#         a = int(a)
#         if a > 0 and a < 10:
#             a -= 1
#             if str(pole[a]) != '*': 
#                 print('Эта ячейка уже занята !')
#                 step -= 1
#             else: pole = pole[:a] + sign + pole[a+1:]
#             vision_pole(pole)
#             if len(check_win(sign)) != 0:
#                 print(f'Победу одержали {sign} на {step} ходу ')
#                 print(f'Игра закончена!')
#                 break
#             step += 1
#             if step == 10: 
#                 res = -1
#                 print(f'Игра закончена! Ничья! ')


# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. 
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето 
# на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы эту фигню можно было прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
# print(' ================================')
# print('Чистим текст от паразитов')
# print('')
# in_text = str('«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. \
#     Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, \
#     в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой \
#     дорогой и не упал в эту… ээээ… яму. Хлеба купил».')
# musor = ['в общем', 'короче говоря', 'ясен пень', 'как бы', 'эээээ', 'ээээ', 'ну', 'короче',  'эээ', 'кажется', 'кстати'] # Сначала пишем словосочетаня !!!! и длинные ээээ

# def remove_m(in_t,mus):
#     in_t = list((in_t.lower()).split('.'))
#     s = ''
#     for l in in_t:
#         for i in mus:
#             l = l.replace(i+', ','')
#             l = l.replace(i+',','')
#             l = l.replace(', '+i,'')
#             l = l.replace(' '+ i,'')
#             l = l.replace(i,'')
#             l = l.replace('  ','')
#         s += l + '.'
#     return s

# print(remove_m(in_text,musor))



"""
4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования, другой — 
с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера 
и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в 
делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. 
Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: 
https://www.charset.org/utf-8 Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce 
сложите получившиеся числа и верните из функции в качестве ответа.
# """
from functools import reduce
print(' ================================')
print('ничего сложного')
print('')
# Создание двух списков
name_lang_list = ['Basic', 'C', 'Fortan', 'FoxPro', 'Java', 'Pascal', 'Delfi', 'Perl', 'PHP', 'VB', 'Phyton']
index_lang_list = [i+1 for i in range(0,len(name_lang_list))]

# Функция создаст список кортежей, состоящих из номера и языка, написанного большими буквами
def kortez_num_name(nls,ils):
    data = list(zip(ils,[i.upper() for i in nls]))
    return data

# Функция создаст список кортежей, состоящих из суммы очков и языка
def utf_kort(nls,ils):

    t_l = [ reduce(lambda x,y: x + ord(y), i, 0) for i in nls ]    # Вымученная строка с reduce, аналог оригинальной строки ниже 
    print(f'Вывод с reduce : \t{t_l}')
    
    t_l=[(sum([ord(i[r]) for r in range(0,len(i))])) for i in nls]  # Оригинальная строка без reduce
    print(f'Вывод без reduce : \t{t_l}')
    
    
    t_l=[(t_l[i],nls[i]) for i in range(len(ils)) if t_l[i]%ils[i] == 0]
    return t_l

print(kortez_num_name(name_lang_list,index_lang_list))
print(utf_kort(name_lang_list,index_lang_list))
