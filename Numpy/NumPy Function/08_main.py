import numpy as np

Value = np.array([2, 81, 4, 10, 2, 20, 47, 96, 4, 45, 47, 64, 81, 10, 96, 20, 100])

result = np.unique(Value, return_index=True)
print(f"Array: {result}")