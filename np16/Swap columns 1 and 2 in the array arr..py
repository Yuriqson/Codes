import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr,'\n\n')
print(arr[::,[1,0,2]])