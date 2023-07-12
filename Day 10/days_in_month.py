"""Module providingFunction that checks the days of a month"""
def is_leap(year):
    """ Defines if the year is leap or not"""
    if year % 4 == 0: #1
        if year % 100 == 0: #2
            if year % 400 == 0: #3
                return True #4
            else: #3
                return False #4
        else: #2
            return True #3
    else: #1
        return False #2

def days_in_month(year, month):
    """ Defines the  number of days of a month"""
    if month > 1 or month <1:
        return "invalid month"
    if is_leap(year) is True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
