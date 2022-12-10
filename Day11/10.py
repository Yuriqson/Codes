def capitalize_list_items(*stuff):
    l=[*stuff]
    new=[]
    for i in l:
        new.append(i.capitalize())
    return new
print(capitalize_list_items('abacaxi','banana','caderno'))