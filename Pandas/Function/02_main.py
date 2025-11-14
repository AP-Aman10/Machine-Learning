import pandas as pd

Value1 = pd.DataFrame({"Num":[1, 2, 3, 4, 5], "Var1":[2, 20, 47, 81, 100]})
Value2 = pd.DataFrame({"Num":[1, 2, 3, 4, 5], "Var2":[4, 10, 45, 64, 96]})

result = pd.concat([Value1, Value2], axis=1, keys=["Value1", "Value2"])
print(f"Concat of Value: \n{result}")