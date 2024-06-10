# Import NumPy
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", array_2d)

# Perform arithmetic operations
array_sum = array_1d + 10
print("Array after adding 10:", array_sum)

array_square = array_1d ** 2
print("Array elements squared:", array_square)

# Use some NumPy built-in functions
mean = np.mean(array_1d)
print("Mean of 1D array:", mean)

max_value = np.max(array_2d)
print("Max value in 2D array:", max_value)

reshape_array = np.reshape(array_1d, (5, 1))
print("Reshaped 1D array to 5x1:\n", reshape_array)

# Generate arrays using NumPy functions
zeros_array = np.zeros((2, 3))
print("2x3 array of zeros:\n", zeros_array)

ones_array = np.ones((3, 2))
print("3x2 array of ones:\n", ones_array)

# Generate an array with a range of values
range_array = np.arange(0, 10, 2)
print("Array with range of values:", range_array)
