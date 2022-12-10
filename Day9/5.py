x=True
while x==True:
    month=str(input('Type the month')).capitalize()
    if month=='September' or month=='October' or month=='November':
        print('It is Autumn season')
    elif month=='December' or month=='January' or month=='February':
        print('the season is Winter')
    elif month=='March' or month=='April' or month=='May':
        print('the season is Spring.')
    elif month=='June'or month=='July' or month=='August':
        print('the season is Summer')
    else:
        break