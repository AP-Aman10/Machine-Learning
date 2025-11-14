import numpy as np
np.set_printoptions(precision=2)

Value = np.matrix([[4, 10], [45, 96]])

result = np.linalg.matrix_power(Value, -2)

print(f"Original Matrix (Value): \n{Value}")
print()
print(f"Linalg Matrix Power Matrix (result): \n{result}")