import numpy as np

Value1 = np.array([4, 10, 45, 64, 96])
Value2 = np.array([[2], [20], [47], [82], [100]])

result = Value1 + Value2
print("--- Result of Broadcasting ---")
print(f"Shape of Value1: {Value1.shape}")
print(f"Shape of Value2: {Value2.shape}")
print(f"Result: \n{result}")