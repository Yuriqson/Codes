import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
sepallength = iris_2d[:, 0].astype('float') #sttig both as float for te calculation
petallength = iris_2d[:, 2].astype('float')
volume = (np.pi * petallength * (sepallength**2))/3
volume = volume[:, np.newaxis] #generating a column for the volume values
out = np.hstack([iris_2d, volume]) #putting the generated column at the array
print(out[:])
"""
numpy.newaxis
A convenient alias for None, useful for indexing arrays.
"""