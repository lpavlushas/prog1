from PIL import Image ,ImageDraw, ImageFont

def z1():
    im = Image.open('new.jpg')
    im2 = im.crop((20,20,440,440))
    im2.show()
    im2.save('im2.JPG')
z1()
