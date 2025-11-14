import numpy as np

value = [[2, 4, 10, 20, 45], [47, 64, 81, 96, 100]]

result = np.array(value)
print(f"Array: \n{result}")
print(f"Number of dimensions: {result.ndim}")
print(f"Shape: {result.shape}")

ReShape = result.reshape(5, 2)
print(f"Reshaped Array: \n{ReShape}") 
print(f"Shape: {ReShape.shape}")