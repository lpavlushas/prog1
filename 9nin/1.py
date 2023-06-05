import csv
import os
from PIL import Image, ImageFilter
def z1():
    a = ('PNG')
    os.mkdir('new')
    for i in os.listdir():
         if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new/' + str(i))
z1()