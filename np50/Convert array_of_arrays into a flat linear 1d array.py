import numpy as np
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

array_of_arrays = np.array([arr1, arr2, arr3])
#print(array_of_arrays)
"""# Solution 1
arr_2d = np.array([a for arr in array_of_arrays for a in arr])
print(arr_2d)
"""
# Solution 2:
arr_2d = np.concatenate(array_of_arrays) #much more comprehensible for reading
print(arr_2d)