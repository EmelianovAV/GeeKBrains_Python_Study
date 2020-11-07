"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков)."""

import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('task_7_less_5.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'There is no average profit. Everyone works at a loss.')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit of each company - {profit}')

with open('task_7_less_5.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Result in json: \n '
          f' {js_str}')

# *******************пример от преподавателя (НЕРАБОТАЕТ)******************

# import json
#
# result = []
# with open('task_7_less_5.json', 'w', encoding='utf-8') as write_f:
#     with open('task_7_less_5.txt', encoding='utf-8') as f_obj:
#         profit = {}
#         for line in f_obj:
#             profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
#         average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
#         result.append(profit)
#         result.append({"average_profit": round(average_profit)})
#     json.dump(result, write_f)

