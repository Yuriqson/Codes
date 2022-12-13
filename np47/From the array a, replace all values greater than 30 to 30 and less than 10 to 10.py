import numpy as np, sys

np.set_printoptions(precision=2)
np.random.seed(100)
a = np.random.uniform(1,50, 20)
print(np.clip(a, a_min=10, a_max=30))
#Solution 2:
#print(np.where(a < 10, 10, np.where(a > 30, 30, a))) ???

"""
random.uniform(low=0.0, high=1.0, size=None)
Draw samples from a uniform distribution.
Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes 
high). In other words, any value within the given interval is equally likely to be drawn by uniform.

numpy.clip(a, a_min, a_max, out=None, **kwargs)
Clip (limit) the values in an array.
Given an interval, values outside the interval are clipped to the interval edges. For example, if an 
interval of [0, 1] is specified, values smaller than 0 become 0, and values larger than 1 become 1.
Equivalent to but faster than np.minimum(a_max, np.maximum(a, a_min)).
No check is performed to ensure a_min < a_max.
"""