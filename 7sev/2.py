def z2():
    img = Image.open('ars.jpg')
    img.show()
    new = img.resize((img.width // 3, img.height // 3))
    new.save("new.png")
    con = img.rotate(188)
    con.save('pov.png')
    con = img.transpose(Image.FLIP_lEFT_RIGHT)
    con.save('pov2.png')


z2()
