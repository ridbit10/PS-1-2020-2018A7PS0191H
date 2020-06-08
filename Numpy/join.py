import numpy as np

a=np.array(10)
b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,9],[3,4,10]],[[5,6,11],[7,8,12]]])

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
for x in arr:
    print(x)

print()

c1=np.array([[1,2,3],[4,5,6]])
c2=np.array([[11,12,13],[14,151,16]])
arr=np.concatenate((c1,c2),axis=0)
for x in arr:
    print(x)

print()

arr=np.concatenate((c1,c2),axis=1)
for x in arr:
    print(x)

print()

arr=np.stack((c1,c2),axis=0)
for x in arr:
    print(x)

print()

arr=np.stack((c1,c2),axis=1)
for x in arr:
    print(x)

print()

arr=np.hstack((c1,c2))
for x in arr:
    print(x)

print()

arr=np.vstack((c1,c2))
for x in arr:
    print(x)

print()

arr=np.dstack((c1,c2))
for x in arr:
    print(x)
