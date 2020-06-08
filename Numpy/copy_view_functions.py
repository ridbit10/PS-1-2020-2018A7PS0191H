import numpy as np

a=np.array([1,2,3,4])
x=a.copy()
y=a.view()
x[0]=42
print(x)
print(a)#changes are not reflected back
y[0]=42
print(y)
print(a)#changes are reflected back

a[0]=37
print(x)#change not reflected
print(y)#changes are still reflectes

print(x.base)#none bcoz it is copy
print(y.base)#array a is its base
