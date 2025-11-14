import numpy as np

# Original 1D array
value = np.array([2, 4, 10, 20, 45, 47, 64, 81, 96, 100])

# Resize the array to 5 rows and 2 columns
reshaped = np.resize(value, (5, 2))

# Flatten the reshaped array in column-major (Fortran-style) order
flattened = reshaped.flatten(order='F')

# Print the results with clearer descriptions
print(f"Original 1D array:\n{value}")
print(f"\nReshaped to 5x2 array:\n{reshaped}")
print(f"\nFlattened (column-major order):\n{flattened}")