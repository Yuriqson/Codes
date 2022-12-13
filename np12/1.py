import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c=np.setdiff1d(a,b)
print(c)

"""a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.setdiff1d(a,b)
print(c)
----------------------------------------------------
numpy.setdiff1d(ar1, ar2, assume_unique=False)
Find the set difference of two arrays.
Return the unique values in ar1 that are not in ar2.
"""
