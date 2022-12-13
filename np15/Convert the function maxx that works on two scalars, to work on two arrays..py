import numpy as np
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
print(maxx(1, 5),'\n\n')
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max=np.vectorize(maxx,[float])
print(pair_max(a,b))

"""
class numpy.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)[source]
Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs and 
returns a single numpy array or a tuple of numpy arrays. The vectorized function evaluates pyfunc over 
successive tuples of the input arrays like the python map function, except it uses the broadcasting rules
 of numpy.
The data type of the output of vectorized is determined by calling the function with the first element of the input. This can be avoided by specifying the otypes argument.
"""