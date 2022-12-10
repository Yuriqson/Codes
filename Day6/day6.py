#1
empty_tuple=()
#2
sister=('Maria','Madalena')
brother=('Jose','Jesus')
#3
sister_l=list(sister)
brother_l=list(brother)
siblings=sister_l+brother_l
#4
print(len(siblings))
#5
momdad=['Holy Spirit','God']
family_members=momdad+siblings
tuple(family_members)
print(family_members)
#ex2
mom,dad,sister1,sister2,brother1,brother2=family_members

fruits=('avocado','banana','orange','apple')
vegetables=('egplant','carrot')
animal=('jauheliha','chicken','beef')
fruits_l=list(fruits)
vegetables_l=list(vegetables)
animal_l=list(animal)
food_stuff_l=fruits_l+vegetables_l+animal_l
food_stuff_tp=tuple(food_stuff_l)
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
food_stuff_lt.pop(3)
print(food_stuff_lt)
food_stuff_lt.pop(0)
food_stuff_lt.pop(0)
food_stuff_lt.pop(0)
food_stuff_lt.pop(-1)
food_stuff_lt.pop(-1)
food_stuff_lt.pop(-1)
print(food_stuff_lt)
food_stuff_tuple2=(food_stuff_lt)
del food_stuff_lt
print(''in food_stuff_tuple2)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)