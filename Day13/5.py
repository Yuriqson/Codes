l = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_list=[i for sublist in l for i in sublist]
flated_flat_list=[i for sublist in flat_list for i in sublist]
p='country: '
c='city: '
new_format=[{p+flated_flat_list[j]:c+flated_flat_list[j+1]} for j in range(0,5,2)]
print(new_format)
