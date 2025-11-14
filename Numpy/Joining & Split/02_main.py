import numpy as np

Value_1 = np.array([[4, 10], [45, 96]])
Value_2 = np.array([[2, 20], [47, 100]])

result = np.concatenate((Value_1, Value_2), axis=0)
print(f"Array after Concatenate: \n{result}")