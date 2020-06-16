from PIL import Image
import numpy as np

im =Image.open('messi.png')
w,h = im.size
left = w/4
right =3*w/4
top=h/4
bottom=3*h/4
im=im.crop((left,top,right,bottom))
im.show()
