import numpy as np
np.random.seed(100)
a = np.random.randint(1,10, [5,3])
print(a)
# Solution 1
#print(np.amax(a, axis=1))

# Solution 2
print(np.apply_along_axis(np.max, arr=a, axis=1))

"""
numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
Return the maximum of an array or maximum along an axis.

numpy.apply_along_axis(func1d, axis, arr, *args, **kwargs)
Apply a function to 1-D slices along the given axis.
Execute func1d(a, *args, **kwargs) where func1d operates on 1-D arrays and a is a 1-D slice of 
arr along axis.
"""