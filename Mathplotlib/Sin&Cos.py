import numpy as np
from matplotlib import pyplot as plt 

x=[1,6,10,4,7]
y=[5,4,3,2,1]

x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   

plt.subplot(2, 1, 1)
plt.plot(x, y_sin) 
plt.title('Sin')  
    
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos) 
plt.title('Cos')  
   
plt.show()
