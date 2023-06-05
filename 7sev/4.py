def z4():
    image1 = Image.open("ink.png")
    new1 = image1.resize((image1.width // 4, image1.height // 4))
    img = Image.open("1.jpg")
    img.paste(new1)
    img.save("inki.jpg")


z4()
