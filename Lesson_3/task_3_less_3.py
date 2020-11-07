"""Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает
сумму наибольших двух аргументов."""


def my_func(arg1, arg2, arg3):
    my_dict = [arg1, arg2, arg3]
    min_arg = min(arg1, arg2, arg3)
    my_dict.remove(min_arg)
    return sum(my_dict)


print(
    f'result - {my_func(int(input("enter first digit ")), int(input("enter second digit ")), int(input("enter third digit ")))}')
