import numpy as np
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a))) #[ 0 -2  2  0 -2  2]
#print(doublediff)
peak_locations = np.where(doublediff == -2)[0] + 1
print(peak_locations)

"""
numpy.diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>)
Subtracts the first number of the array by its second, then the second by the third, and so on.

numpy.sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
 = <ufunc 'sign'>
Returns an element-wise indication of the sign of a number.
The sign function returns -1 if x < 0, 0 if x==0, 1 if x > 0. nan is returned for nan inputs.
"""