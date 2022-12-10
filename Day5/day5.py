#1
empty_list=[]
#2
list_more_than_five=[1,2,3,4,5,6]
#3
print(len(list_more_than_five))
#4
print(list_more_than_five[0],list_more_than_five[3],list_more_than_five[-1])
#5
mixed_data_types=['Yuri',22,1.75,'single','Linnunradankatu 13 A 8']
#6
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0],it_companies[3],it_companies[-1])
#10
it_companies[0]='IT'
print(it_companies)
#11
it_companies.insert(0,'Another IT company')
print(it_companies)
#12
it_companies.insert(3,'middle company')
print(it_companies)
#13
it_companies[-4].upper()
#14
print('#; '.join(it_companies))
#15
print('Apple' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
it_companies.pop(0)
it_companies.pop(1)
it_companies.pop(2)
print(it_companies)
#19
it_companies.pop(-1)
it_companies.pop(-1)
it_companies.pop(-1)
print(it_companies)
#20
it_companies.pop(1)
#21
it_companies.pop(0)
#22
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.pop(3)
#23
it_companies.pop(-1)
#24
it_companies.clear()
#25
del it_companies
#26
front_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node','Express', 'MongoDB']
addition=front_end+back_end
print(addition)
#27
full_stack=addition.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)