""" Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

with open('task_2_less_5.txt', 'r+', encoding='utf-8') as my_file:
    content = my_file.readlines()
    print(f'Line number`s {len(content)}')
    for index, value in enumerate(content):
        number_of_words = len(value.split())
        print(f'\nLine number {index + 1} has {number_of_words} words.')




