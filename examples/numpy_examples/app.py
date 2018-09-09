import numpy as np

# a = np.array([1,2,3])
# print(a)

import time, sys
S = range(1000)
print(sys.getsizeof(5)* len(S))

D = np.arange(1000)
print(D.size * D.itemsize)
