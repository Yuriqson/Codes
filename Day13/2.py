l =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list=[i for sublist in l for i in sublist]
#print(flat_list)
flated_flat_list=[i for sublist in flat_list for i in sublist]
print(flated_flat_list)