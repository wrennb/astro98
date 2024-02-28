def digital_root(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

# Testing code:
n = 12345
print(digital_root(n))  