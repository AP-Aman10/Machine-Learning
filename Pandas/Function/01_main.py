import pandas as pd

Value1 = pd.DataFrame({"Num":[1, 2, 3, 4, 5, 6], "Var1":[2, 20, 47, 81, 100, 26]})
Value2 = pd.DataFrame({"Num":[1, 2, 3, 4, 5, 7], "Var2":[4, 10, 45, 64, 96, 74]})

result = pd.merge(Value1, Value2, how="outer", indicator=True)
print(f"Result of Value: \n{result}")