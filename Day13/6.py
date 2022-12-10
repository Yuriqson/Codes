l= [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flat_list=[i for sublist in l for i in sublist]
flated_flat_list=[i for sublist in flat_list for i in sublist]
print(flated_flat_list)
