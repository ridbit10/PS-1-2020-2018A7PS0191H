import numpy as np

a=np.array(['geeks', 'is', 'me'])
print(np.char.count(a,'geek'))
print(np.char.count(a, 'e'))
print(np.char.rfind(a,'geek'))
print(np.char.rfind(a, 'e'))
