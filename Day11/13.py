def sum_all_numbers(num):
    sum=0
    for value in range(1,num+1):
        sum=sum+value
    return sum
print(sum_all_numbers(int(input('What number?'))))