import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a,'\n\n')
print(b,'\n\n')
print(np.vstack([a, b]),'\n\n')
print(np.concatenate([a, b], axis=0),'\n\n')
print(np.r_[a, b])

#print(np.concatenate([a, b], axis=-1),'\n\n')
#print(np.concatenate([a, b], axis=1),'\n\n')


"""
numpy.r_ = <numpy.lib.index_tricks.RClass object>
Translates slice objects to concatenation along the first axis.
"""