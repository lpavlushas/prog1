def z3():
    name = ["1.jpg", "2.jpg", "3.jpg"]
    for file in name:
        with Image.open(file) as img:
            img.load()
            new1 = img.filter(ImageFilter.CONTOUR)
            new1.show()
            new1.save('new' + file)


z3()