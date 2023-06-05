def z2():
    try:
        n = int(input("Введите число: "))
        v = 100 / n
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("Введен 0!")
    else:
        print(f"100 : {n} = {v}")