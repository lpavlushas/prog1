def z2():
    a = ('.jpg', '.PNG')
    os.mkdir('new2')
    for i in os.listdir():
        if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new2/' + str(i))