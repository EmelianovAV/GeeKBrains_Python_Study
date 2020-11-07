"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает
 учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
 предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
 типы занятий. Сформировать словарь, содержащий название предмета и общее количество
 занятий по нему. Вывести словарь на экран."""

subj = {}
with open('task_6_less_5.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        timing = []
        subject = ([el for el in line.split(" ")])
        for el in subject:
            timing.append(''.join(i for i in list(el) if i.isdigit()))
        subj[line.split(':')[0]] = sum([int(i) for i in timing if i.isdigit()])


print(subj)


#************2 вариант от преподавателя****************
#
# import re
#
# subj = {}
#
# with open('task_6_less_5.txt', encoding='utf-8') as init_f:
#     for line in init_f.readlines():
#         subj[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
#     print(subj)
