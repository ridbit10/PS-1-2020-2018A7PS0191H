import numpy as np
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
#ma-min
print(np.percentile(a,50))
print(np.percentile(a,50,axis=0))
print(np.percentile(a,50,axis=1))
