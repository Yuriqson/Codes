def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            print('No')
            return
    return print('Yes')
is_prime(int(input('What number')))