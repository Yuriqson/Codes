import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(np.corrcoef(iris[:, 0], iris[:, 2])[0, 1])

"""
numpy.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>, *, dtype=None)
Return Pearson product-moment correlation coefficients.
is a measure of linear correlation between two sets of data. It is the ratio between the 
covariance of two variables and the product of their standard deviations
"""