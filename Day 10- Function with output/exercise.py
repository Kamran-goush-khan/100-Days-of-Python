def is_leap_year(year):
    """This function take year as input and tell whether the input year is a leap year or not"""
    # Write your code here.
    if year % 4 == 0 :
        if year % 400 == 0 :
            return True
        elif year % 4 == 0 and year % 100 != 0 :
            return True
        else :
            return False
    else :
        return False
    # Don't change the function name.
print(is_leap_year(2004))