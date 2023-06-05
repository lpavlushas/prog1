def z3():
    d = input("Введите дату: ")
    d = d.split(".")
    if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
        print("Дата магическая, ура!")
    else:
        print("Дата не магическая")