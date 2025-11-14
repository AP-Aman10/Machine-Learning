import numpy as np

value = [[2, 4, 10, 20, 45], [47, 64, 81, 96, 100]]

result = np.array(value, ndmin=4)
print(f"Array: \n{result}")
print(f"Number of dimensions: {result.ndim}")
print(f"Shape: {result.shape}")