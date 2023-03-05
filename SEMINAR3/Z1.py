"""
Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""

import random



my_list = [random.randint(1,10) for _ in range(10)]
print(my_list)

number = int(input('Введите число: '))

count = 0
number_new = 0 
difference = 0
difference_two = number
for i in my_list:
    if i == number:
       count +=1
       if count == 0:
          print(f'Введенное вами число встречается {count} раз')
    difference = i - number
    if difference < 0:
       difference *= -1
    if difference < difference_two:
       difference_two = difference
       number_new = i
print(f'Введенное вами число встречается {count} раз')  
if count == 0:
    print(f'Eсть число {number_new}')
