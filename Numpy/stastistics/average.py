import numpy as np
a = np.array([1,2,3])
#ma-min
print(np.average(a))
wts=np.array([1,2,3])
print(np.average(a,weights=wts))
print(np.average(a,weights=wts,returned=True))
