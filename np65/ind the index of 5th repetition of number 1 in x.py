import numpy as np
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5
# Solution 1: List comprehension
#print([i for i, v in enumerate(x) if v == 1][n-1])
# Solution 2: Numpy version
print(np.where(x == 1)[0][n-1]) #more understandable