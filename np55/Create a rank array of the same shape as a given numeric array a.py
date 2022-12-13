import numpy as np
np.random.seed(10)
a = np.random.randint(20, size=[2,5])
print(a)
print(a.ravel().argsort().argsort().reshape(a.shape))

"""
chararray.ravel([order])
Return a flattened array.

chararray.reshape(shape, order='C')
Returns an array containing the same data with a new shape.
"""