import pandas as pd

Value = [2, 4, 10, 20, 45, 47, 64, 81, 96, 100]
result = pd.Series(Value, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

print(f"Series: \n{result}")
print(f"Type of Series: {type(result)}")