import numpy as np, sys
np.random.seed(100)
a = np.random.uniform(1,50, 20)
#print(a.argsort()) #bad
# Solution 2:
print(np.argpartition(-a, 5)[:5]) #good

"""
# Below methods will get you the values.
# Method 1:
a[a.argsort()][-5:]

# Method 2:
np.sort(a)[-5:]

# Method 3:
np.partition(a, kth=-5)[-5:]

# Method 4:
a[np.argpartition(-a, 5)][:5]

numpy.argpartition(a, kth, axis=- 1, kind='introselect', order=None)
Perform an indirect partition along the given axis using the algorithm specified by the kind keyword.
 It returns an array of indices of the same shape as a that index data along the given axis in partitioned
 order.
"""