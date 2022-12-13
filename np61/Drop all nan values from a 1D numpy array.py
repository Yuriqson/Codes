import numpy as np
a=np.array([1,2,3,np.nan,5,6,7,np.nan])
print(a[~np.isnan(a)]) #~ inverts the result. Instead of returning just the nun values, it returns the numbers
#print(a[np.isnan(a)])
#print(~False)
#print(~True)

"""
The bitwise operator ~ (pronounced as tilde) is a complement operator. It takes one bit operand and returns its
 complement. If the operand is 1, it returns 0, and if it is 0, it returns 1
For example if a=60 (0011 1100 in binary) its complement is -61 (-0011 1101) stored in 2's complement
"""