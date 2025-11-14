import numpy as np

Value = np.matrix([[2, 4, 10, 20, 45], [47, 64, 81, 96, 100]])

result = np.swapaxes(Value, 0, 1)

print(f"Original Matrix (Value): \n{Value}")
print()
print(f"Swapaxes Matrix (result): \n{result}")