import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
i, j = np.where(iris_2d)
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
print(iris_2d)

"""
numpy.nan
Floating point representation of Not a Number (NaN).
"""