def z2():
    d = []
    s = [7, 1, 0, 1, 0, 75, 62, 88]
    for x in s:
        if s.count(x) > 1:
            d.append(x)
    print("n2")
    print(*d)
z2()