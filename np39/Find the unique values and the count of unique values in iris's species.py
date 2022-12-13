import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
species = np.array([row.tolist()[4] for row in iris])
print(np.unique(species, return_counts=True))

"""
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, *, 
equal_nan=True)
Find the unique elements of an array.
"""