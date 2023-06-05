from PIL import Image, ImageFilter
def z1():
    Filename = "ars.jpg"
    with Image.open('ars.jpg') as img:
        img.load()
    img.show()
    width, height = img.size

    format = img.format
    mode = img.mode
    print("Width:", width)
    print("Height:", height)
    print("Format:", format)
    print("Color Model:", mode)


z1()