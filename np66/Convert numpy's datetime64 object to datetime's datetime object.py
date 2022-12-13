import numpy as np
from datetime import datetime
dt64 = np.datetime64('2022-12-13 15:50:10')
from datetime import datetime
print(dt64.tolist())
#print(np.dtype(dt64))

"""
class numpy.datetime64
If created from a 64-bit integer, it represents an offset from 1970-01-01T00:00:00. If created from string, 
the string can be in ISO 8601 date or datetime format.
"""