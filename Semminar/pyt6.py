# Шифр Цезаря

text = 'Это шифрованное сообщение'
smesh = 5


print(f'Исходный текст: {text}')
def encod(txt,S):
    data = [chr(ord(i) + S) for i in txt]
    data = ''.join(data)
    return data

en_text = encod(text,smesh)
print(f'Зашифрованное сообщение: {en_text}')

def decod(txt,S):
    data = [chr(ord(i) - S) for i in txt]
    data = ''.join(data)
    return data

en_text = decod(en_text,smesh)
print(f'Расшифрованное сообщение: {en_text}')

# Шифр Атбаш

alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '

text = 'Это шифрованное сообщение'

print(f'Исходный текст: {text}')
def Ancod(txt,al):
    data = [al[len(al) - 1 - al.index(i.upper())] for i in txt]
    data = ''.join(data)
    return data

en_text = Ancod(text,alph)
print(f'Зашифрованное сообщение: {en_text}')

en_text = Ancod(en_text,alph)
print(f'Расшифрованное сообщение: {en_text}')
