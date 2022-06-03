# 1. Напишите программу, удаляющую из текста все слова содержащие "абв". Используйте знания с последней лекции. Выполните ее в виде функции. 
in_text = 'Жили были дед, баба и абвешка, в абв-какой деревушке. Решила абвешка пойти крутабвернуться и абвернулась.'

data = list(map(str,in_text.split()))
list_out = [data.remove(i) for i in data \
    i.split('абв')]
print(data)

#def s

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. 
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето 
# на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы эту фигню можно было прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.


# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых 
# создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем 
# столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.