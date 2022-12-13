import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(np.isnan(iris_2d).any())
#iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3,4])
#print(np.isnan(iris_2d).any()) #True because it is str