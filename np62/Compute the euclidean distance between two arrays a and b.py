import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
dist = np.linalg.norm(a-b)
print(dist)

"""
The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.

linalg.norm(x, ord=None, axis=None, keepdims=False)
Matrix or vector norm.
This function is able to return one of eight different matrix norms, or one of an infinite number of vector norms
"""