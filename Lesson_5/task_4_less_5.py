"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
"""

from translate import Translator

with open('task_4_less_5.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.read()
    translator = Translator(from_lang="english", to_lang="russian")
    translation = translator.translate(content)
with open('task_4_less_5_new.txt', 'w+', encoding='utf-8') as new_file:
    new_file.write(translation)

# # *********************2 вариант********************
#
# my_dict = {"one": "Один", "two": "два", "three": "три", "four": "четыре"}
#
# with open('task_4_less_5_new.txt', 'a', encoding=('utf-8')) as new_file:
#     with open('task_4_less_5.txt', encoding=('utf-8')) as my_file:
#         line = my_file.read().split("\n")
#         for i in line:
#             i = i.split(" - ")
#             new_file.writelines(my_dict[i[0] + ' - ' + i[1] + '\n'])
