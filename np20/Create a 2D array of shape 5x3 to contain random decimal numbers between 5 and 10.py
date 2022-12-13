import numpy as np
# Input
arr = np.arange(9).reshape(3,3)

rand_arra = np.random.randint(5,10,(5,3))+np.random.random((5,3))
print(rand_arra,'\n\n')

rand_arrb = np.random.uniform(5,10, size=(5,3))
print(rand_arrb,'\n\n')
#print(sum(rand_arrb,rand_arra))