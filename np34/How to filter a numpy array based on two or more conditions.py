import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print(iris_2d[condition])