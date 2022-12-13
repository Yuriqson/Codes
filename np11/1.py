import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
print(c)

#d=list(set(a)&set(b))
#print(d) #not an array, because of the commas

"""
numpy.intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
Find the intersection of two arrays.
Return the sorted, unique values that are in both of the input arrays.
Input arrays. Will be flattened if not already 1D
"""