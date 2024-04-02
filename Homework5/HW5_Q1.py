import numpy as np
def findEqual(array):
    equal_array = []
    for row in array:
        if len(set(row)) == 1:  
            equal_array.append(row)
    return equal_array
arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
equal_array = findEqual(arr)
print(equal_array)