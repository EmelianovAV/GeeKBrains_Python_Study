"""Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""


my_list = []
while True:
    data = input("Enter any word: ")
    if data == '':
        print(my_list)
        exit()
    else:
        data_list = data + '\n'
        my_list.append(data_list)

    with open("task_1_less_5.txt", "w", encoding="utf-8") as file_obj:
        file_obj.writelines(my_list)