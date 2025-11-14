import pandas as pd

Value = {
    "Name": ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"],
    "Hindi": [91, 67, 82, 79, 54, 58],
    "English": [86, 72, 96, 82, 68, 70],
    "Maths": [99, 79, 86, 90, 64, 68],
    "Science": [84, 69, 88, 77, 54, 64],
    "SST": [88, 70, 95, 75, 58, 66]
}

result = pd.DataFrame(Value)
Total = result["Maths"] + result["English"] + result["Hindi"] + result["Science"] + result["SST"]
result["Percentage"] = ((Total / 500) * 100).round(2)

print(result)