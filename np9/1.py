import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a,'\n\n')
print(b,'\n\n')
print(np.concatenate([a, b], axis=1),'\n\n')
print(np.hstack([a, b]),'\n\n')
print(np.c_[a, b])

"""
numpy.c_ = <numpy.lib.index_tricks.CClass object>
Translates slice objects to concatenation along the second axis.
"""