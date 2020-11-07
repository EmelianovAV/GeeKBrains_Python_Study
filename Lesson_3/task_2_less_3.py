"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def my_funk(name, surname, b_year, town, email, phone_number):
    return ' '.join([name, surname, b_year, town, email, phone_number])


print(
    my_funk(name='Ilon', surname='Musk', b_year='1976', town='Washington', email="123@123.com",
            phone_number='+12345678'))

"""2"""
def my_funk_2(**kwargs):
    return kwargs


print(my_funk_2(name=input("Enter your name: "), surname=input("Enter your surname: "),
                b_year=input("Enter your b_year: "), town=input("Enter your town: "),
                email=input("Enter your email: "), phone_number=input("Enter your phone: ")))
