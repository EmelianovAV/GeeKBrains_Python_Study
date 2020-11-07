""" Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль —
выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

deb = int(input("Enter your company's profit for the year: "))
cred = int(input("Enter your company's expenses for the year: "))
if deb <= cred:
    print ("Your company is unprofitable.")
if deb > cred:
    profit = deb - cred
    print("Profitability of your company's revenue", profit, "$")
    human = int(input("Enter the number of employees in your company: "))
    human_profit = profit / human
    print("Company's profit per employee", human_profit, "$")