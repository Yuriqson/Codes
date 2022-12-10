def sum_odd(numo):
    sum=0
    for value in range(1,numo+1,2):
        sum=sum+value
    print(sum)
def sum_even(nume):
    sum=0
    for value in range(0,nume+1,2):
        sum=sum+value
    print(sum)
sum_odd(int(input('What number')))
sum_even(int(input('Another number')))