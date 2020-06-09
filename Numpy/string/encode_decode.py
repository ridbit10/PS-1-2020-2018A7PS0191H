import numpy as np
x = np.array(['Messi', 'aA', 'abcdefg'])
print("x:", x)
e = np.char.encode(x, encoding='cp037')
print("\nAfter encoding: ",e)
d = np.char.decode(e, encoding='cp037')
print("\nAfter decodeing: ",d)
