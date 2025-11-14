import numpy as np

Value = np.array([2, 4, 10, 20, 45, 47, 64, 81, 96, 100])

print(f"Array: {Value}")
result = np.where((Value % 4) == 0)
print(f"Indices where values are divisible by 4: {result}")