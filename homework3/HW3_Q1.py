def pow(x, y):
    answer = 1
    for _ in range(y):
        answer *= x
    return answer

# Using the code for two to the third power
x = 5
y = 2
print(pow(x, y))