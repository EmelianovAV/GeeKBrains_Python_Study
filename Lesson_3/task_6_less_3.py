"""Реализовать функцию int_func(), принимающую слово из маленьких
 латинских букв и возвращающую его же, но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text."""


def int_func(*args):
    up_word = input("enter word's with space: ").title()
    return print(up_word)


int_func()
