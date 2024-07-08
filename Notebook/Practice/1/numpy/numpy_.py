import numpy as np

# Create a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])
print("Original array:")
print(arr)

# Accessing elements
print("\nAccessing elements:")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice of array:", arr[2:4])

# Array shape and dimensions
print("\nArray shape and dimensions:")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)

# Reshaping array
print("\nReshaping array:")
arr_reshaped = arr.reshape(5, 1)
print(arr_reshaped)

# Array operations
print("\nArray operations:")
arr2 = np.array([6, 7, 8, 9, 10])
print("Array 2:", arr2)
print("Addition:", arr + arr2)
print("Subtraction:", arr - arr2)
print("Multiplication:", arr * arr2)
print("Division:", arr / arr2)

# Universal functions (ufunc)
print("\nUniversal functions:")
print("Square root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Sin:", np.sin(arr))

# Statistical functions
print("\nStatistical functions:")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
