#Задача 2: Найдите сумму цифр трехзначного числа.


threedigit_number = int(input('Введите трехзначное число: '))
sum = ((threedigit_number % 10) + ((threedigit_number // 10) % 10) + (threedigit_number // 100))
print(f'Сумма цифр: {sum} ')
