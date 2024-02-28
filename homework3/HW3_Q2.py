def find_values(values):
# If the list is empty
    if not values: 
        return None, None
# Initialize min and max with the first element of the list
    min = max = values[0]  

    for i in values:
        if i < min:
            min = i
        elif i > max:
            max = i

    return min, max

# Testing my code
list1 = [87, 1, 0, 56, 16, 9, 101, 6, 32, 3]
min, max = find_values(list1)
print("Minimum value:", min)
print("Maximum value:", max)