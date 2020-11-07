"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения."""

from itertools import count, cycle


def my_count(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)


def my_cycle(my_list, iteration):
    arg = 0
    func = cycle(my_list)
    while arg < iteration:
        print(func)
        arg += 1


my_count(start_num=int(input("enter start number: ")), stop_num=int(input("enter stop number: ")))
my_cycle(my_list=[1, 2, 3, 4], iteration=int(input("enter iteration: ")))
