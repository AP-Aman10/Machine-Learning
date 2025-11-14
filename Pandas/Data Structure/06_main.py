import pandas as pd

Value_1 = pd.Series([4, 10, 45, 64, 96])
Value_2 = pd.Series([2, 20, 47, 81, 100])

result = Value_1 + Value_2
print(f"Series: \n{result}")