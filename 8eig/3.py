def z3():
    name = input("vvedite imia:")
    filename = "dr.jpg"
    with Image.open(filename) as img:
        img.load()
        font = ImageFont.truetype("Sequência.otf", 30)
        draw_text = ImageDraw.Draw(img)
        draw_text.text(
            (img.width // 2 - 100, 15),
            name + ",pozdravlau!",
            font=font,
            fill=('red')
        )
        img.show()
        img.save(name + "birth2.png")
z3()