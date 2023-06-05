def z2():
    otk = {"день победы":"9may.jpg", "международный женский день":"8mart.jpg", "новый год":"ng.jpg"}
    k =input("Какой праздник?")
    if k in otk:
        image = Image.open(otk[k])
        image.show()
    else:
        print("net otkritki")
z2()