"""*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя."""

goods = []
features = {'title': '', 'cost': '', 'lot': '', 'unit': ''}
analytics = {'title': [], 'cost': [], 'lot': [], 'unit': []}
num = 0
while True:
    if input('for quit press Q, to continue press Enter: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Enter the property value "{f}": ')
        features[f] = int(_) if (f == 'cost' or f == 'lot') else _
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f'\n current product analytics: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)
