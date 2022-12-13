import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
print(iris_2d[:4])

"""
chararray.tolist()
Return the array as a list
"""