def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        res=print('It is Autumn season')
        return res
    elif month == 'December' or month == 'January' or month == 'February':
        res=print('the season is Winter')
        return res
    elif month == 'March' or month == 'April' or month == 'May':
        res=print('the season is Spring.')
        return res
    elif month == 'June' or month == 'July' or month == 'August':
        res=print('the season is Summer')
        return res
    return res
check_season(input('What month?').capitalize())