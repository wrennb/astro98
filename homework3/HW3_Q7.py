def vowel_count(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

# Example usage:
input_str = "UC Berkeley"
print(vowel_count(input_str))  # Output: 4