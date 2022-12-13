import numpy as np
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)
# Create an all True array
out = np.full(a.shape[0], True)
#print(out)
#print(a.shape[0])
# Find the index positions of unique elements
unique_positions = np.unique(a, return_index=True)[0]
#print(unique_positions)
# Mark those positions as False
out[unique_positions] = False
print(out)

"""
numpy.full(shape, fill_value, dtype=None, order='C', *, like=None)
Return a new array of given shape and type, filled with fill_value.
"""