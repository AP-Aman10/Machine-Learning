import numpy as np
np.set_printoptions(precision=2)

Value1 = np.array([4, 10, 45, 64, 96])
Value2 = np.array([100, 82, 47, 20, 2])


print(f"Value1: {Value1} =><= Value2: {Value2}")
print()
print("--- Arithmetic Operations ---")
print(f"Addition : {np.add(Value1, Value2)}\n")
print(f"Subtraction : {np.subtract(Value1, Value2)}\n")
print(f"Multiplication : {np.multiply(Value1, Value2)}\n")
print(f"Division : {np.divide(Value1, Value2)}\n")
print(f"Modules : {np.mod(Value1, Value2)}\n")
print(f"Exponentiation : {np.power(Value1, Value2)}")