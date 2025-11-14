import numpy as np

Value = np.array([2, 4, 10, 20, 45, 47, 64, 81, 96, 100])

print(f"Array: {Value}")
result = np.searchsorted(Value, [66, 67, 68, 69],side='right')
print(f"Insertion index for [66, 67, 68, 69]: {result}")