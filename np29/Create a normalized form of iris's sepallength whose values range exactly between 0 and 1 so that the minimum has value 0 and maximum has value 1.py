import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin) #normalized form
"""To normalize a vector in math means to divide each of its elements
to some value V ((Smax - Smin) in this case) so that the length/norm of the resulting vector is 1.
Turns out the needed V is equal to the length (norm) of the vector."""
print(S)
#or
#S = (sepallength - Smin)/sepallength.ptp()
"""
numpy.ptp(a, axis=None, out=None, keepdims=<no value>)[source]
Range of values (maximum - minimum) along an axis.
The name of the function comes from the acronym for ‘peak to peak’.
"""
