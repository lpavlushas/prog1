def p3():
    en_ru = open('en-ru.txt ', encoding="utf-8").read().split('\n')
    s = {}
    for i in range(len(en_ru)):
        en_ru[i] = en_ru[i].split(' - ')
        s[en_ru[i][0]] = en_ru[i][1:]
    print(s)

    s1 = {}
    for i in s:
        for k in s[i]:
            k = k.split(', ')
            for j in k:
                if j not in s1:
                    s1[j] = i
                else:
                    s1[j] = s1[j] + ', ' + i
    s1 = dict(sorted(s1.items()))
    print(s1)

p1(), p2(), p3()