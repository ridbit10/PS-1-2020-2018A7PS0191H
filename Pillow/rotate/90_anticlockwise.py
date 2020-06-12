from PIL import Image
import numpy as np

im =Image.open('messi.png')
im=im.rotate(90)
im.show()

