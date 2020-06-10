import numpy as np
from matplotlib import pyplot as plt 
#from pylab import *

x=[1,6,10,4,7]
y=[5,4,3,2,1]

x=np.arange(-3,3,0.1)
y=np.sin(x)   
plt.plot(x,y,'r.')
y=np.cos(x)
plt.plot(x,y,'b.')
y=-np.sin(x)
plt.plot(x,y,'k--')
plt.show()
