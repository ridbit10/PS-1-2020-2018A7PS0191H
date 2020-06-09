import numpy as np

a=np.array(10)
b=np.array([10,3,6,1,7,4])
c=np.array([[4,2],[8,5]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

print(c.T)
print(np.linalg.inv(c))
