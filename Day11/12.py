lst=['Abacaxi','Banana','Carambola']
def remove_item(lst,item):
    res=lst.remove(item)
    return res
print(lst)
remove_item(lst,'Banana')
print(lst)