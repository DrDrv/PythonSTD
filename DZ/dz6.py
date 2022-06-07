# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;



# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 
print(' ================================')
print('RLE алгоритм')
print('')
filename_in = 'dz6_book.txt'
filename_out = 'dz6_encodebook.txt'
filename_or = 'dz6_decodebook.txt'

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
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.