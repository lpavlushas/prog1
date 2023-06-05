def n4():

    from random import randint
    print("для завершение напишите Стоп")
    while True:
        x=randint(1,100)
        y=randint(1,100)
        print(f"{x}+{y}=",end="")
        result=input()
        if result == "Стоп":
            break
        result=int(result)
        if x+y==result:
            print("Правильно")
        else:
            print("неПравильно")

n4()