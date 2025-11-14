import numpy as np

Value_1 = np.matrix([[20, 47], [2, 100]])
Value_2 = np.matrix([[96, 45], [10, 4]])

result = Value_1 % Value_2
print(f"Modulus Value_1 % Value_2: \n{result}")