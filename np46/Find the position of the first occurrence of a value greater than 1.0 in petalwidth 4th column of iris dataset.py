import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
print(np.argwhere(iris[:, 3].astype(float) > 1.0)[0]) #[0] is the position

"""
numpy.argwhere(a)
Find the indices of array elements that are non-zero, grouped by element.
"""