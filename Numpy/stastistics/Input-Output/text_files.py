import numpy as np 

a=np.array([1,2,3,4,5]) 
np.savetxt('out23.txt',a) 
b=np.loadtxt('out23.txt') 
print (b)
