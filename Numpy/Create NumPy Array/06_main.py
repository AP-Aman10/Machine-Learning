import numpy as np

Value = [[2, 4, 10, 45, 96], [100, 82, 64, 47, 20]]
result = np.array(Value, ndmin=4)

print(f"Multi-D Array: \n{result}")
print(f"Shape: {result.shape}")
print(f"Dimension: {result.ndim}")