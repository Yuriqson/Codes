import random
def list_gen():
    j=0
    while j!=7:
        random_num=random.randint(0,9)
        l.append(random_num)
        j+=1
    return l
def unique_values(g):
    s = set()
    for x in g:
        if x in s: return False
        s.add(x)
    return True
l = []
l=list_gen()
while unique_values(l)==False:
    l.clear()
    list_gen()
print (l)