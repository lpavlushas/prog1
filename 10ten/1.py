import json

def p1():
    with open('10lab.json', encoding="utf-8") as f:
        s = json.load(f)
    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('available: true')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')
