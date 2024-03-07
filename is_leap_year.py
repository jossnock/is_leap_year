def is_leap_year(year):
    """Pass in a year (don't specift AD or BC)
    If the year is a leap year, returns True
    If the year isn't a leap year, returns False"""
    if year % 4 != 0:
        return False
    if year % 100 == 0:
        if year % 400 == 0:
            return False
        return True
    return True

assert(is_leap_year(2016)==True)
assert(is_leap_year(2005)==False)
assert(is_leap_year(400)==False)
assert(is_leap_year(700)==True)
    
year = input("Input a year to see if it's a leap year (don't specift AD or BC):")
print(is_leap_year(year))

