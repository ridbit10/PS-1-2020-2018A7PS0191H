import numpy as np

a=np.array(10)
b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

newb=b.reshape(2,3,2)
print(newb)
print(newb.base)
b[6]=89
print(newb)

print()

newc=c.reshape(-1)
print(newc)

print()

e=np.array([1,2,3,4,5,6])
newe=e.reshape(2,-1)
print(newe)
