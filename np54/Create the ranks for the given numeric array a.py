import numpy as np
np.random.seed(10)
a = np.random.randint(20, size=10)
print(a)
print(a.argsort().argsort()) #ranking a rank

"""
numpy.argsort(a, axis=- 1, kind=None, order=None)
Returns the indices that would sort an array.
Perform an indirect sort along the given axis using the algorithm specified by the kind keyword. It 
returns an array of indices of the same shape as a that index data along the given axis in sorted order.
"""