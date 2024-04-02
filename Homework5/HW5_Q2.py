import numpy as np

def checkerboard():
    array = np.zeros((8, 8), dtype=int)
    array[::2, ::2] = 1  #Setting alternate rows
    array[1::2, 1::2] = 1  #Setting alternate columns
    return array

result = checkerboard() #Printing result
print(result)