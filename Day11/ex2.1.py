def even_and_odds(num):
    l=list(range(0,num))
    if num%2==0:
        print('Even')
        sum_e = len(l) / 2 + 1
        print('Number of even', sum_e)
    elif num==1:
        print('Number of odds: 1')
    else:
        sum_o = len(l) / 2
        print('Number of odds:', sum_o)

even_and_odds(int(input('What number')))