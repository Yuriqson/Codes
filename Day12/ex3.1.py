import random
l=[1,2,3,4,5]
print(l)
def rand_list(lst):
    random.shuffle(lst)
    print(lst)
rand_list(l)
