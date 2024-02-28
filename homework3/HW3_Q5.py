def rotation(n):
    # Getting the last digits
    last = n % 10 
    # Getting the remaining digits
    other = n // 10 
    # Defining variable
    i = 0
    temp = other

    # Count the number of digits
    while temp > 0:
        i += 1
        temp //= 10

    rotated_number = last * (10 ** i) + other
    return rotated_number

# Example usage:
n = 12345
rotated_n = rotation(n)
print(rotated_n)  # Output: 51234