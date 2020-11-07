"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


def my_func():
    try:
        with open('task_5_less_5.txt', 'w+', encoding='utf-8') as my_func:
            line = input('Enter numbers separated by a space: ')
            my_func.writelines(line)
        with open('task_5_less_5.txt', 'r', encoding='utf-8') as my_func:
            my_numb = my_func.read()
            my_numb = my_numb.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in the file')
    except ValueError:
        print('Wrong number dialed. I/o error')


my_func()
