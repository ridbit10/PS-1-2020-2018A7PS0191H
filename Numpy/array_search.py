import numpy as np

a=np.array([1,4,6,9,4])

x=np.where(a==4)
print(x)

print()

x=np.where(a%2==0)
print(x)

print()

srt=np.array([1,5,5,7,9,13])

x=np.searchsorted(srt,5)
print(x)

x=np.searchsorted(srt,5,side='right')
print(x)

x=np.searchsorted(srt,[5,6,7])
print(x)
