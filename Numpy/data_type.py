import numpy as np

a=np.array([1,2,3,4])
b=np.array([100000000000000000,2,3,4])
c=np.array(['messi','suarez','neymar'])
print(a.dtype)
print(b.dtype)
print(c.dtype)

a=np.array([1,2,3,4],dtype='S')
print(a.dtype)

x=np.array([0.1,1.2,2.6])
newx = x.astype('i')
print(newx)
print(newx.dtype)
newx2 = x.astype(int)
print(newx2)
print(newx2.dtype)

newx3 = newx.astype(bool)
print(newx3)
print(newx3.dtype)
