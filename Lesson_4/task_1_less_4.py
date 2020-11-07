"""Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами."""

from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Result  {res}')
except ValueError:
    print('Not a number')



# Пример преподователя
# from sys import argv
#
# def result():
#     try:
#         time, salary, bonus = map(float, argv[1:])
#         print(f"Result: {time * salary + bonus}")
#     except ValueError:
#         print("Enter right numbers.")
#
# result()

