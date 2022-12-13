import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
print(np.percentile(sepallength, q=[5, 95]))

"""
numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, 
interpolation=None)
Compute the q-th percentile of the data along the specified axis.
Returns the q-th percentile(s) of the array elements.
"""