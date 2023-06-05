def z1():
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Введено не число!")
    else:
        if number % 3 == 0:
            print(f"{number} делится на 3")
        elif number == 0:
            print("Введен 0!")
        else:
            print(f"{number} не делится на 3")
z1()