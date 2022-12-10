x=True
fruits = ['banana', 'orange', 'mango', 'lemon']
while x==True:

    new_fruit=str(input('Type a fruit')).lower()
    if new_fruit=='break':
        print('Closing...')
        break
    elif new_fruit=='list':
        print(fruits)
    elif new_fruit in fruits:
        print('This fruit is already in the list')
    elif new_fruit not in fruits:
        fruits.append(new_fruit)
        print('The fruit was added to the list')
        print(fruits)


