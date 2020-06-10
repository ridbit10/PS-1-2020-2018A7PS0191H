import numpy as np
from matplotlib import pyplot as plt
import math  
#from pylab import 
x=np.array([])
for i in range(-30,30,1):
    x=np.append(x,[i/10])
y=np.array([])
for i in x:
    y=np.append(y,[math.sqrt(9-(i*i))])
plt.plot(x,y)
plt.plot(x,-y)

plt.show()
