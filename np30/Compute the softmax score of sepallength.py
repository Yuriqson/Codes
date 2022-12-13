import numpy as np, sys
url = r"C:\Users\yuccq\OneDrive\Área de Trabalho\PythonProjects\NumpyProjects\iris.data"
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
np.set_printoptions(3) # precision
"""The softmax function, converts a vector of K real numbers into a probability distribution of K
 possible outcomes."""

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
print(softmax(sepallength))