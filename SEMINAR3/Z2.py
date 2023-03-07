"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков
    Напишите программу, которая вычисляет стоимость введенного пользователем слова.
    Будем считать, что на вход подается только одно слово, которое содержит либо
    только английские, либо только русские буквы.
"""

eng = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y'
scrabble_eng_ = {}
scrabble_eng_['1'] = '[A, E, I, O, U, L, N, S, T, R ]'
scrabble_eng_['2'] = '[D, G]'
scrabble_eng_['3'] = '[B, C, M, P ]'
scrabble_eng_['4'] = '[F, H, V, W, Y ]'
scrabble_eng_['5'] = '[K]'
scrabble_eng_['8'] = '[J, X]'
scrabble_eng_['10'] = '[Q, Z ]'

rus = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'
scrabble_rus_ = {}
scrabble_rus_['1'] = '[А, В, Е, И, Н, О, Р, С, Т ]'
scrabble_rus_['2'] = '[Д, К, Л, М, П, У ]'
scrabble_rus_['3'] = '[Б, Г, Ё, Ь, Я]'
scrabble_rus_['4'] = '[Й, Ы ]'
scrabble_rus_['5'] = '[Ж, З, Х, Ц, Ч ]'
scrabble_rus_['8'] = '[Ш, Э, Ю]'
scrabble_rus_['10'] = '[Ф, Щ, Ъ ]'


word = input('Введите слово на английском или русском языке: ')

if word.lower() in eng:
    sum = 0
    for i in word:
        for key, value in scrabble_eng_.items():
            if i.upper() in value:
              sum += key
    print(f'Стоимость введенного слова = {sum}')

elif word.lower() in rus:
    sum = 0
    for i in word:
        for key, value in scrabble_rus_.items():
            if i.upper() in value:
               sum += key
    print(f'Стоимость введенного слова = {sum}')
        
