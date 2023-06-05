def z4():
    print("n4")
    import random
    g1=('Иванов','Филипенко','Юниверс','Разумовский','Волков')
    g2 = ('Гром', 'Пчелкина', 'Дубин', 'Дагбаев', 'Макарова')
    x1=[]
    x2=[]
    x=[]
    x1.append(random.sample(g1,5))
    x2.append(random.sample(g2,5))
    x.extend(*x1)
    x.extend(*x2)
    x=tuple(x)
    print('a', x)
    print('b',g1)
    print('b', g2)
    print('b', x)
    print('c', len(x))
    print('d', *sorted(x))
    print('e', 'Иванов' in x)
    print('e', x.count('Иванов'))
z4()