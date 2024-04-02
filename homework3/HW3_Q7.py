def vowel_count(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

# Testing code:
input_str = "UC Berkeley"
print(vowel_count(input_str)) 