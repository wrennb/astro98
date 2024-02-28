def leap_year(year):
    # Checking for divisibility by 4, 100, and 400
    if year % 4 == 0: 
        if year % 100 == 0:  
            if year % 400 == 0:  
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Testing code:
year = 2024
print(leap_year(year))  # Output: True