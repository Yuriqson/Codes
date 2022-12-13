import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
#print(iris)
species = iris[:, 4] #species column
# Approach 1: Generate Probablistically
"""np.random.seed(100) #"starting point of a fixed generated-random-result", like controlling the random result. This part is in the code probably to generate the same result as the tutorial.
a = np.array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
species_out = np.random.choice(a, 150, p=[0.5, 0.25, 0.25])
print(species_out)"""
# Approach 2: Probablistic Sampling (preferred)
#Approach 2 is preferred because it creates an index variable that can be used to sample 2d tabular data.
np.random.seed(100) 
probs = np.r_[np.linspace(0, 0.500, num=50), np.linspace(0.501, .750, num=50), np.linspace(.751, 1.0, num=50)] #generating species array
index = np.searchsorted(probs, np.random.random(150))
species_out = species[index]
print(np.unique(species_out, return_counts=True))
"""
random.choice(a, size=None, replace=True, p=None)
Generates a random sample from a given 1-D array

char.chararray.searchsorted(v, side='left', sorter=None)
Find indices where elements of v should be inserted in a to maintain order.

numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
Return evenly spaced numbers over a specified interval.
Returns num evenly spaced samples, calculated over the interval [start, stop].
The endpoint of the interval can optionally be excluded.
"""