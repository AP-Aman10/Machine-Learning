import pandas as pd

result = pd.DataFrame({
    "Value_1": [True, False, True, False],
    "Value_2": [True, False, False, True]
})

result["Or"] = result["Value_1"] | result["Value_2"]
result["And"] = result["Value_1"] & result["Value_2"]
print(f"DataFrame of [Or] and [And]: \n{result} ")