import numpy as np

Value1 = 96
Value2 = 4

print(f"Value1: {Value1} =><= Value2: {Value2}")
print()
print("--- Arithmetic Operations ---")
print(f"Addition =>  {Value1} + {Value2}: {np.add(Value1, Value2)}")
print(f"Subtraction =>  {Value1} - {Value2}: {np.subtract(Value1, Value2)}")
print(f"Multiplication =>  {Value1} * {Value2}: {np.multiply(Value1, Value2)}")
print(f"Division =>  {Value1} / {Value2}: {np.divide(Value1, Value2)}")
print(f"Modules =>  {Value1} % {Value2}: {np.mod(Value1, Value2)}")
print(f"Exponentiation =>  {Value1} ^ {Value2}: {np.power(Value1, Value2)}")