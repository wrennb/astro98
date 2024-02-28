def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Testing code:
weight = 72  # kilograms
height = 2  # meters
bmi = calculate_bmi(weight, height)
print("This BMI is:", bmi)