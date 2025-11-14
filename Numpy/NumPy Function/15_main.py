import numpy as np

Value = np.array(["A", "D", "F", "J", "K", "M", "N", "P", "R", "S"])
ValueT = [True, True, False, True, True, False, False, True, False, True]

result = Value[ValueT]
print(f"Array Filter: {result}")