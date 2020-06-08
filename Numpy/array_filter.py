import numpy as np

a=np.array(10)
b=np.array([10,3,6,1,7,4])
c=np.array([[4,2,3],[8,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

fltr=[]

for x in b:
    if(x%2):
        fltr.append(True)
    else:
        fltr.append(False)

print(b[fltr])

fltr1=b>5
print(b[fltr1])

fltr2=b%2==0
print(b[fltr2])
