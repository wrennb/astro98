import numpy as np

def spaceBetween(array):
    separation = []
    for string in array:
        separated_string = ' '.join(string)
        separation.append(separated_string)
    return separation

# Example usage:
my_arr = np.array(['python', 'is', 'cool'])
result = spaceBetween(my_arr)
print(result)