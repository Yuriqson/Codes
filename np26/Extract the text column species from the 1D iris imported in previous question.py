import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)

species = np.array([row[4] for row in iris_1d])
print(species[:5])
