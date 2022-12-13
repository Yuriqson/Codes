import numpy as np
arr = np.arange(10)
print(arr,'\n\n')
arr=arr.reshape(2,5)
print(arr,'\n\n')
arr2=np.arange(1,10)
print(arr2,'\n\n')
arr2=arr2.reshape(3,-1)
print(arr2)