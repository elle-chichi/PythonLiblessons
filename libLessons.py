import numpy as np

# Creating a NumPy array
a = np.array([1,2,3])
print(a)

# Creating a 2D NumPy array:
b = np.array([[1,2,3],[4,5,6]])
print(b)

# Using NumPy functions to perform mathematical operations on arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

# addition
print(a+b)
# subtraction
print(b-a)
# multiplication
print(a*b)
# division
print(b/a)
# Slicing and indexing NumPy arrays
a = np.array([1,2,3,4,5])
# indexing
print(a[0])
print(a[-1])
#  slicing
print(a[1:4])
# Reshaping NumPy arrays
a = np.array([1,2,3,4,5,6,7,8,9])
# Reshape to a 3x3 array
b = a.reshape((3,3))
print(b)