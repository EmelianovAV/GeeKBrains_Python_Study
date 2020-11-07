"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

some_number = int(input("Enter a positive number "))
max_digit = some_number % 10
while some_number >= 1:
    some_number = some_number // 10
    if some_number % 10 > max_digit:
        max_digit = some_number % 10
    if some_number > 9:
        continue
    else:
        print("Maximum digit in a number", max_digit)
