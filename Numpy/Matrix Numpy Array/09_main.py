import numpy as np
np.set_printoptions(precision=2)

Value = np.matrix([[4, 10], [45, 96]])

result = np.linalg.inv(Value)

print(f"Original Matrix (Value): \n{Value}")
print()
print(f"Linalg Matrix (result): \n{result}")