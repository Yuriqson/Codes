import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
print(a[(a >= 5) & (a <= 10)],'\n\n')
index = np.where((a >= 5) & (a <= 10))
print(a[index],'\n\n')
index = np.where(np.logical_and(a>=5, a<=10))
print(a[index])

"""
numpy.logical_and(x1, x2, /, out=None, *, where=True,casting='same_kind', order='K', dtype=None,
 subok=True[, signature, extobj]) = <ufunc 'logical_and'>
Compute the truth value of x1 AND x2 element-wise.
"""