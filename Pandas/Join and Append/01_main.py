import pandas as pd

Value1 = pd.DataFrame({"Val1": [4, 10, 45, 64, 96], "Val2": [2, 20, 47, 81, 100]}, index=["A", "B", "C", "D", "E"])
Value2 = pd.DataFrame({"Val3": [14, 30, 55, 74, 86], "Val4": [12, 40, 57, 71, 90]}, index=["A", "B", "C", "D", "E"])

result = Value1.join(Value2)
print(f"Join [Value1 + Value2]: \n{result}")