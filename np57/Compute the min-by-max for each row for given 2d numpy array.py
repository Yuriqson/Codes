import numpy as np
np.random.seed(100)
a = np.random.randint(1,10, [5,3])
print(a)
print(np.apply_along_axis(lambda x: np.min(x)/np.max(x), arr=a, axis=1)) #taking the min value of each row and dividing by the max, and putting into an array