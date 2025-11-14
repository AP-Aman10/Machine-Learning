import numpy as np

Value = [[[10, 4], [45, 96]], [[100, 64], [47, 20]]],
result = np.array(Value)

print(f"Array: \n{result}")
print(f"Array: {result[0, 0, 0 , 0]}")
print(f"Array: {result[0, 0, -2, -1]}")