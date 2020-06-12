from PIL import Image
import numpy as np

im =Image.open('messi.png')
deg=int(input())
im=im.rotate(deg)
im.show()

