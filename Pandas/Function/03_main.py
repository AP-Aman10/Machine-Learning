import pandas as pd

Value = {
    "Val": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Num1": [2, 4, 10, 20, 45, 47, 64, 81, 96, 100],
    "Num2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

result = pd.DataFrame(Value)
result_New = result.groupby("Val")
print(f"Value: \n{result}")
print(f"Result New: {result_New}")