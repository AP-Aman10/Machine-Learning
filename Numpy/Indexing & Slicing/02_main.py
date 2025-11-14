import numpy as np

Value = [[[2, 4, 10, 45, 96], [100, 81, 64, 47, 20]]]
result = np.array(Value)

print(f"Array: \n{result}")
print(f"Array: {result[0, 0 ,4]}")
print(f"Array: {result[0, 1, -1]}")