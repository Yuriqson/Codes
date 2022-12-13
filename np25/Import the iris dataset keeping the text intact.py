import numpy as np
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data" #converts normal string to raw string
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris[:3])

"""
numpy.genfromtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, skip_header=0, skip_footer=0,
 converters=None, missing_values=None, filling_values=None, usecols=None, names=None, excludelist=None, 
 deletechars=" !#$%&'()*+, -./:;<=>?@[\\]^{|}~", replace_space='_', autostrip=False, case_sensitive=True,
  defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True, max_rows=None, 
  encoding='bytes', *, ndmin=0, like=None)
Load data from a text file, with missing values handled as specified.
Each line past the first skip_header lines is split at the delimiter character, and characters following 
the comments character are discarded.
"""