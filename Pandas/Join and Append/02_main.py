import pandas as pd

Value1 = pd.DataFrame({"Val1": [4, 10, 45, 64, 96], "Val2": [2, 20, 47, 81, 100]})
Value2 = pd.DataFrame({"Val3": [14, 55, 86], "Val4": [12, 40, 71]})

result = pd.concat([Value1, Value2], ignore_index=True)
print(f"Append [Value1 + Value2]:\n{result}")