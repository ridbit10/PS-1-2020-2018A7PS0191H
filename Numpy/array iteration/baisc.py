import numpy as np

a=np.array(10)
b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

for x in d:
    print(x)

print()
    
for x in d:
    for y in x:
        print(y)

print()

for x in d:
    for y in x:
        for z in y:
            print(z)


