import numpy as np

a=np.array(10)
b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

for idx,x in np.ndenumerate(d):
    print(idx,x)
