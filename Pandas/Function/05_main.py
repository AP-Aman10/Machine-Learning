import pandas as pd

Value = {
    "Val": ["B", "A", "A", "C", "A", "B", "D", "B", "A", "C"],
    "Num1": [2, 4, 10, 20, 45, 47, 64, 81, 96, 100],
    "Num2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

result = pd.DataFrame(Value)
result_New = result.groupby("Val")

print(f"Sum of [Num1] + [Num2]: \n{result_New.sum()}")
print(f"Max of Find the Smallest: \n{result_New.max()}")
print(f"Min of Find the Biggest: \n{result_New.min()}")