import pandas as pd

Value = {"Num_1": [100, 81, 47, 20, 2], "Num_2": [4, 10, 45, 64, 96]}
result = pd.DataFrame(Value)

result["+"] = result["Num_1"] + result["Num_2"]
result["-"] = result["Num_1"] - result["Num_2"]
result["*"] = result["Num_1"] * result["Num_2"]
result["/"] = (result["Num_1"] / result["Num_2"]).round(2)
print(f"DataFrame of Value: \n{result}")