import numpy as np

a=np.array(10)
b=np.array([1,2,3,4,5,6,7,8,9,10])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

print(b[1:5])
print(b[1:])
print(b[:6])
print(b[::2])
print(b[-3:-1])
print(b[-7:-1:2])
print(c[1,1:])
print(d[1,0,::2])
print(d[1,0:2,1:2])
