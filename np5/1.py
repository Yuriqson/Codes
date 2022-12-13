import numpy
arr = numpy.array(range(10))
arr[arr % 2 == 1] = -1
print(arr)