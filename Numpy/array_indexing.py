import numpy as np

a=np.array(10)
b=np.array([1,2,3])
c=np.array([[1,2],[1,2]])
d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(d[0,1,1])
print(d[-2,-1,-1])
print(d[0,0,1])
