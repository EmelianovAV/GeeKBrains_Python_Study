"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369"""

some_number = input("Enter some number 'n': ")
num_1 = some_number
num_2 = some_number + some_number
num_3 = some_number + some_number + some_number
num_sum = int(num_1) + int(num_2) + int(num_3)
print("The sum of the numbers n + nn + nnn is", num_sum)