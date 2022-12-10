def reverse_list(*stuff):
    l=[*stuff]
    l.reverse()
    return l
print(reverse_list('a','b','c','d','e'))
print(reverse_list(1,2,3,4,5))