"""Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников."""

summa = 0
count = 0
persons = []
with open('task_3_less_5.txt', "r", encoding="utf-8") as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000 {poor}, средняя величина дохода сотрудников {sum(map(float, sal)) / len(sal)}')
