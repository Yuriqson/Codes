import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
petal_len_setosa = iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float') #filtering the desired column
#print(petal_len_setosa)
# Get the second last value
#print(np.unique(np.sort(petal_len_setosa))) #this is in progressive order
print(np.unique(np.sort(petal_len_setosa))[-2]) #printing the one the exercise asks