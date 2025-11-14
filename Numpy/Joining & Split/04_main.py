import numpy as np

Value_1 = np.array([4, 10, 45, 64, 96])
Value_2 = np.array([2, 20, 47, 81, 100])

result = np.stack((Value_1, Value_2))
print(f"Array after Stack: \n{result}")