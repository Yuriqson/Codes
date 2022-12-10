l = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_list=[i for sublist in l for i in sublist]
#print(flat_list)
flated_flat_list=[i for sublist in flat_list for i in sublist]
flated_flat_list.insert(1,'FIN')
flated_flat_list.insert(4,'SWE')
flated_flat_list.insert(7,'NOR')
print(flated_flat_list)
new_format=[(flated_flat_list[i],flated_flat_list[i+1],flated_flat_list[i+2]) for i in range(0,7,3)]

print(new_format)
