lst0 =[1,2,3,4,'banana']
lst1 =['abacaxi','banana','melancia']
def homogeneous_type(lst):
    iseq=iter(lst)
    first_type=type(next(iseq))
    return first_type if all((type(i)is first_type)for i in iseq) else False
print(homogeneous_type(lst0))
print(homogeneous_type(lst1))