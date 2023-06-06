cost = {}
cost['А'] = cost['В'] = cost['Е'] = cost['И'] = cost['Н'] = cost['О'] = cost['Р'] = cost['С'] = cost['Т'] = 1
cost['Д'] = cost['К'] = cost['Л'] = cost['М'] = cost['П'] = cost['У'] = 2
cost['Б'] = cost['Г'] = cost['Ё'] = cost['Ь'] = cost['Я'] = 3
cost['Й'] = cost['Ы'] = 4
cost['Ж'] = cost['З'] = cost['Ч'] = cost['Ц'] = cost['Х'] = 5
cost['Ш'] = cost['Э'] = cost['Ю'] = 8
cost['Ф'] = cost['Щ'] = cost['Ъ'] = 10

a = input()
d = 0
for i in a:
    i = i.upper()
    d += cost[i]
print(d)