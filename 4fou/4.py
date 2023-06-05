def z4():
    ch = input("Введите номер билета: ")
    x = 0
    y = 0
    if len(ch) % 2 == 0:
        for i in ch[0:int(len(ch) / 2)]:
            x = x + int(i)
        for i in ch[int(len(ch) / 2):int(len(ch)) + 1]:
            y = y + int(i)
        if x == y:
            print("Билет счастливый!")
        else:
            print("Билет не является счастливым!")
    else:
        print("Количество цифр нечётно!")
z4()