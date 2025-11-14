import numpy as np

Value = np.array([2, 4, 10, 20, 45, 47, 64, 81, 96, 100])

result = np.resize(Value, (2, 5))
print(f"Array: {Value}")
print(f"Array: \n{result}")