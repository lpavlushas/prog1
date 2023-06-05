def p2():
    with open('10lab.json', 'r', encoding='utf8') as f:
        s = json.load(f)

    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('name')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')
        print('')

    dop = {}
    dop['name'] = input('Название: ')
    dop['price'] = input('Цена: ')
    dop['available'] = input('В наличии?: ')
    dop['weight'] = input('Вес: ')

    s['products'].append(dop)

    with open('10lab.json', 'w', encoding='utf8') as f:
        json.dump(s, f, indent=4, ensure_ascii=False)
        print(s)
