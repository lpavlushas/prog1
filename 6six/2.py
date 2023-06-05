def z2():
    och={
        1 : ['А','В','Е','И','Н','О','Р','С','Т'],
        2 : ['Д','К','Л','М','П','У'],
        3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        4 : ['Й', 'Ы'],
        5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        6 : ['Ш', 'Э', 'Ю'],
        7 : ['Ф', 'Щ', 'Ъ'],
    }
    print('n2:')
    x = input("Vvedite slovo")
    x=list(x)
    d=0
    for i in x:
        for k in och:
            if i in och[k]:
                d+=k
    print('vashe slovo stoit', d, 'ballov')
z2()