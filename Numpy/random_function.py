from numpy import random

x=random.randint(100)#integer from 0 to 100
print(x)

x=random.rand()#float 0 to 1
print(x)

x=random.choice([10,11,8,17.3])
print(x)
#creating array with different sizes

x=random.randint(100,size=(3,5))
print(x)

x=random.rand(4,6)
print(x)

x=random.choice([3,5,7,11],size=(5))
print(x)
