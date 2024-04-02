# Minimum value using a for loop
def find_min_for(num):
    if not num:
        return None  # When the list is empty
    
    min_for = num[0]
    for i in num:
        if i < min_for:
            min_for = i
    return min_for

# Minimum value using a while loop
def find_min_while(num):
    if not num:
        return None  # When the list is empty
    
    min_while = num[0]
    i = 1
    while i < len(num):
        if num[i] < min_while:
            min_while = num[i]
        i += 1
    return min_while

# Maximum value using a for loop
def find_max_for(num):
    if not num:
        return None  # When the list is empty
    
    max_for = num[0]
    for i in num:
        if i > max_for:
            max_for = i
    return max_for

# Maximum value using a while loop
def find_max_while(num):
    if not num:
        return None  # When the list is empty
    
    max_while = num[0]
    i = 1
    while i < len(num):
        if num[i] > max_while:
            max_while = num[i]
        i += 1
    return max_while

# Testing code
num = [45, 32, 19, 22, 57, 131]

print("Minimum with for loop:", find_min_for(num))
print("Minimum with while loop:", find_min_while(num))
print("Maximum with for loop:", find_max_for(num))
print("Maximum with while loop:", find_max_while(num))