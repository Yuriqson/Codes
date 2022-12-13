import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# Solution
#labeling the columns
numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species
# List comprehension version
[[group_val, numeric_column[grouping_column==group_val].mean()] for group_val in np.unique(grouping_column)]
# For Loop version
output = []
for group_val in np.unique(grouping_column):
    output.append([group_val, numeric_column[grouping_column==group_val].mean()])
print(output)