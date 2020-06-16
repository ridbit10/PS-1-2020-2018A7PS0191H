from PIL import Image
import numpy as np

im1 =Image.open('messi.png')
im2=Image.open('messi3.png')
w,h = im2.size
left = w/4
right = w/2
top=h/5
bottom=h/2
im2=im2.crop((left,top,right,bottom))
im1.paste(im2,(170,50))
im1.show()
