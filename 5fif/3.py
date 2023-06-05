def z3():
    print("n3")
    week = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
    x = int(input('ВВедите кол-во выходных '))
    for i in week:
        print('рабочие:', *week[:-x])
        print('Выходные:', *week[-x:])
        break
z3()