def z3():
    sum = 0
    A = True
    with open("data.csv", "r") as file:
        file = csv.reader(file)
        for i in file:
            if A:
                A = False
            else:
                print(i)
                products = i[0]
                kolvo = i[1]
                cena = i[2]
                print(f"{products} - {kolvo} шт. за ", int(cena) * int(kolvo), " руб.")
                sum += int(kolvo) * int(cena)
    print(f"Итоговая сумма: {sum} руб.")
z3()