import numpy as np

Value = np.array([2, 4, 10, 20, 45, 47, 64, 81, 96, 100])

print(f"Array: {Value}")
result = np.array_split(Value, 2)
print(f"Array: {result}")
print(f"Array Index[0]: {result[0]}")
print(f"Array Index[1]: {result[1]}")