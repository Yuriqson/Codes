import numpy as np
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

"""
numpy.where(condition, [x, y, ]/)
Return elements chosen from x or y depending on condition.
"""