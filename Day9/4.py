x=True
while x == True :
    grade=int(input('Enter the grade'))
    if 80 <= grade <= 100 :
        print('A')
    elif 70 <= grade <= 79 :
        print('B')
    elif 60<=grade<=69:
        print('C')
    elif 50<=grade<=59:
        print('D')
    elif 0<=grade<=49:
        print('F')
    else :
        break