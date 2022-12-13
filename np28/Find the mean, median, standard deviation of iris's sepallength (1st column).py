import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu,'      ', med,'        ', sd)