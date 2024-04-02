import numpy as np

np.random.seed(12345) #Making and printing random matrix
rand_array = np.random.randint(1, 50, (4, 5))
print("Original array:")
print(rand_array)

sort_array = np.sort(rand_array, axis=0) #Sorting and printing said matrix
print("\nSorted array along the columns:")
print(sort_array)