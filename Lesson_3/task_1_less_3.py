"""Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""


def my_funk():
    dig_one = input("enter first digit: ")
    dig_two = input("enter second digit: ")
    try:
        diff = int(dig_one) / int(dig_two)
        print(f'Result: {diff}')
    except ValueError:
        print("Value Error")
    except ZeroDivisionError:
        print("Wrong! You can't use zero as a divider")


my_funk()
