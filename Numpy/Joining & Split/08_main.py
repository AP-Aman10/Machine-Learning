import numpy as np

Value = np.array([[2, 4, 10, 20, 45], [47, 64, 81, 96, 100]])

print(f"Array: \n{Value}")
result = np.array_split(Value, 1)
print(f"Array: {result}")