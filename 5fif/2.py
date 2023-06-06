def z2():
    d = []
    s = [6, 1, 0, 1, 0, 87, 45, 3]
    for x in s:
        if s.count(x) > 1:
            d.append(x)
    print("n2")
    print(*d)
z2()