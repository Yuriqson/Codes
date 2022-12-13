"""Less than 3 --> 'small', 3-5 --> 'medium', '>=5 --> 'large' """
import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#print(iris)
petal_length_bin = np.digitize(iris[:, 2].astype('float'), [0, 3, 5, 10]) #takes the indices of the desired lengths in an array
#print(petal_length_bin)
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
#print(label_map)
petal_length_cat = [label_map[x] for x in petal_length_bin] #put the lables at the array of indices
print(petal_length_cat[:4])
#print(petal_length_cat)

"""
chararray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
Copy of the array, cast to a specified type.

numpy.digitize(x, bins, right=False)[source]
Return the indices of the bins to which each value in input array belongs.
If values in x are beyond the bounds of bins, 0 or len(bins) is returned as appropriate.
"""