import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
vals, counts = np.unique(iris[:, 2], return_counts=True)
print(vals[np.argmax(counts)])

"""
numpy.argmax(a, axis=None, out=None, *, keepdims=<no value>)
Returns the indices of the maximum values along an axis.
"""