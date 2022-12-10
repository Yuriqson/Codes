lst0 =['abacaxi','banana','melancia','banana']
lst1 =['abacaxi','banana','melancia']
def compare_unique(l):
    if(len(set(l))==len(l)):
        print("All elements are unique.")
    else:
        print("All elements are not unique.")
print(lst0)
compare_unique(lst0)
print(lst1)
compare_unique(lst1)