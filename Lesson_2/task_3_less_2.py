"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

num_month = int(input("Enter number of the month(1-12): "))

my_dict = {1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "may", 6: "jun", 7: "jul",
           8: "aug", 9: "sen", 10: "oct", 11: "nov", 12: "dec"}
my_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sen", "oct", "nov", "dec"]

if num_month in my_dict:
    print(f"{num_month}-th(s) month of the year {my_dict[num_month]}")
    print(f"{num_month}-th(s) month of the year {my_list[num_month - 1]}")
else:
    print("Wrong month")