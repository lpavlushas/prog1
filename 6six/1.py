def z1():
    countries={
        "russia" : "moscow",
        "brazil" : "brazilia",
        "france" : "paris",
        "finland" : "helsinki"
    }
    print('n1:')
    print("a",countries)
    x=input('Vvedite strany ')
    print("b", countries[x])
    print("c", sorted(countries))
z1()