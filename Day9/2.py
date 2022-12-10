#2
x=True
while x == True:

    age=int(input('Enter your age'))
    fixed_age=22
    if age == fixed_age:
        print('We have the same age')
    elif age < fixed_age:
        print('You are younger than me')
    elif age > fixed_age :
        print('You are older than me')
    else :
        break