"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове."""

string = input("enter wort with space:").split()

for n, word in enumerate(string, 1):
    print(f'{n} {word[:10]}')
