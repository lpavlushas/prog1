def z3():
    stu={
        'Валя' : ['eng','rus','spa'],
        'Петя': ['eng', 'rus', 'chi'],
        'Коля': ['eng', 'rus'],
        'Маша': ['rus', 'chi'],
        'Стёпа': ['rus'],
        'Игорь': ['eng', 'spa'],
        'Костя': ['kz', 'rus'],
        'Егор': ['eng', 'it'],
        'Аня': ['eng', 'fr'],
    }
    d = []
    c = 0
    k=[]
    for i in stu:
        for i in stu[i]:
            if i not in d:
                d.append(i)
                c+=1
    for i in stu:
        if 'chi' in stu[i]:
            k.append(i)
        else:
            continue
    print('n3:')
    print(*d)
    print('всего языков:',c)
    print(*(sorted(d)))
    print('знают китайкий', *k)
z3()