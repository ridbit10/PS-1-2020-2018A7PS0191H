from PIL import Image
import numpy as np


im = np.array(Image.open('messi.png'))
print(im.shape)
