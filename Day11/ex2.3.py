import statistics
l=[1,2,3,4,5,2]
def calculate_mean(lst):
    res=sum(lst)/len(lst)
    print('The mean is:',res)
calculate_mean(l)
def calculate_median(lst):
    res=statistics.median(lst)
    print('The median is:',res)
calculate_median(l)
def calculate_mode(lst):
    res=statistics.mode(lst)
    print('The mode is:',res)
calculate_mode(l)
def calculate_range(lst):
    lst.sort()
    res=lst[-1]-lst[0]
    print('The range is:',res)
calculate_range(l)
def calculate_variance(lst):
    res=statistics.variance(lst)
    print('The variance is:',res)
calculate_variance(l)
def calculate_std(lst):
    res=statistics.stdev(lst)
    print('The standard deviation is:',res)
calculate_std(l)