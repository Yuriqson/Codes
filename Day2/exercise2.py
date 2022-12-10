# Day 2: 30 Days of python programming
#1
first_name='Yuri '
last_name='Henriqson Accordi'
full_name= first_name+last_name
country= 'Finland'
city='Riihimäki'
age=22
year=2022
is_married='no'
is_true=True
is_light='yes'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

#2
print(len(first_name))

#3
print('The length of your first name is:',len(first_name),'and the length of your last name is:',len(last_name))

#4
num_one=5
num_two=4
total= num_one + num_two
diff=num_two-num_one
product=num_two*num_one
division=num_one/num_two
remainder=num_two&num_one
exp=num_one**num_two
floor_division=num_one//num_two

#5
area_of_circle=(3.14*30**2)
circum_of_circle= (3.14*2*30)
print('Type the radius')
area=(3.14*int(input())**2)
print('area:',area)

#6
first_name=input('first name')
last_name=input('last name')
country=input('country')
age=input('age')
print(first_name)
print(last_name)
print(country)
print(age)

#7
help()
