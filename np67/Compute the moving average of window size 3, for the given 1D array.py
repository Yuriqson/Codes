import numpy as np
np.random.seed(100)
Z = np.random.randint(10, size=10)
print(Z)
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
# Method 1
print(moving_average(Z, n=3).round(2))
# Method 2:  # Thanks AlanLRH!
# np.ones(3)/3 gives equal weights. Use np.ones(4)/4 for window size 4.
#np.convolve(Z, np.ones(3)/3, mode='valid')

"""
char.chararray.cumsum(axis=None, dtype=None, out=None)
Return the cumulative sum of the elements along the given axis.

Moving average: take the average of the array based o the desired range n=3, then shifting one step until reaching 
the end. So, from [8 8 3 7 7 0 4 2 5 2] [(8+8+3)/3,(8+3+7)/3,...].
"""
