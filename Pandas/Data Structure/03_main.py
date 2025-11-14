import pandas as pd

Value = [2, 4, 10, 20, 45, 47, 64, 81, 96, 100]
result = pd.Series(Value, dtype="float", name="Series")

print(f"Series: \n{result}")
print(f"Type of Series: {type(result)}")