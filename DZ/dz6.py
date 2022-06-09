# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;
# from operator import index


from unittest import result


print(' ================================')
print('Консольный калькулятор')
print('')
operand = ['*','/','+','-', '(',')']
formula = (input(f'Введите выражение: ')).replace(' ','')

# Функция разбивает выражение на числа и операторы и закидывает все это в список
def dev_form(f_la,op_nd):
    tmp = ''
    list_f_la = []
    for i in range(0,len(f_la)):
        if f_la[i] in op_nd:
            if tmp != '': list_f_la.append(tmp)
            tmp = ''
            list_f_la.append(f_la[i])
        else: 
            tmp += f_la[i]
    if tmp != '':list_f_la.append(tmp)
    return list_f_la

def calc(f_la):
    new_formula = []
    for i in f_la:
        if i == '*':
            k = f_la.index(i)
            new_formula.append(int(f_la[k-1]) * int(f_la[k+1]))
        if i == '/':
            k = f_la.index(i)
            new_formula.append(int(f_la[k-1]) / int(f_la[k+1]))
        if i == '+':
            k = f_la.index(i)
            new_formula.append(int(f_la[k-1]) + int(f_la[k+1]))
        if i == '-':
            k = f_la.index(i)
            new_formula.append(int(f_la[k-1]) - int(f_la[k+1]))
    print(new_formula)


    return new_formula

resultat = dev_form(formula,operand)
print(resultat)
resultat = str(calc(resultat)[0])
print(resultat)

# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 
# print(' ================================')
# print('RLE алгоритм')
# print('')
# filename_in = 'dz6_book.txt'
# filename_out = 'dz6_encodebook.txt'
# filename_or = 'dz6_decodebook.txt'

# Функция просто отображения оригинального текста в файле, ну для себя и проверки
# def orig_text(file):
#     with open(file,'r') as f:
#         for i in f:
#             txt = ''.join(str(i)) 
#     return(txt)   
# # Просто нашел алгоритм как он работает и по правилам описал здесь
# def encode_text(file_in,file_out):
#     with open(file_in,'r') as f:
#         for i in f:
#             txt = ''.join(str(i))
#     enc_str = ""
#     i = 0
#     while (i <= len(txt)-1):
#         count = 1
#         ch = txt[i]
#         j = i
#         while (j < len(txt)-1):  
#             if (txt[j] == txt[j + 1]): 
#                 count += 1
#                 j += 1
#             else: 
#                 break
#         enc_str += str(count) + ch
#         i = j + 1
#     with open(file_out,'w') as f:
#         f.write(enc_str) 
#     return enc_str # Вывод в консоль - просто что б видеть
# # Разжатие по правилам
# def decode_text(file_out,file_r):
#     with open(file_out,'r') as f:
#         for i in f:
#             txt = ''.join(str(i))    
#     dec_str = ""
#     i = 0
#     j = 0
#     while (i <= len(txt) - 1):
#         count = int(txt[i])
#         word = txt[i + 1]
#         for j in range(count):
#             dec_str += word
#             j = j + 1
#         i = i + 2
#     with open(file_r,'w') as f:
#         f.write(dec_str)
#     return dec_str # Вывод в консоль - просто что б видеть

# print(f'Оригинальный текст: \n {orig_text(filename_in)}')
# print('')
# print(f'Сжатый текст: \n {encode_text(filename_in,filename_out)}')
# print('')
# print(f'Вернули текст: \n {decode_text(filename_out,filename_or)}')
# print('')


# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть
# возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.
# print(' ================================')
# print(' Шифрование ROT 13')
# print('')
# text = 'This is an encrypted message.'
# alphavit = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
             

# print(f'Исходный текст: {text}')

# def encodecod(txt,al_t):
#     data = txt
#     for i in al_t:
#         for k in range(len(txt)):
#             if i == txt[k]:
#                 if (al_t.index(i) > 0 and al_t.index(i) < 13) or (al_t.index(i) > 25 and al_t.index(i) < 39):
#                     data = data[:k] + al_t[al_t.index(i)+13] + data[k+1:]
#                 if (al_t.index(i) > 12 and al_t.index(i) < 26) or (al_t.index(i) > 38 and al_t.index(i) < 52):
#                     data = data[:k] + al_t[al_t.index(i)-13] + data[k+1:]
#     return data

# en_text = encodecod(text,alphavit)
# print(f'Зашифрованное сообщение: {en_text}')

# en_text = encodecod(en_text,alphavit)
# print(f'Расшифрованное сообщение: {en_text}')