import numpy as np

Value = np.matrix([[4, 10], [45, 96]])

result = np.linalg.matrix_power(Value, 0)

print(f"Original Matrix (Value): \n{Value}")
print()
print(f"Linalg Matrix Power Matrix (result): \n{result}")