import pandas as pd

file_path = r"C:\Users\Aman Patidar\Desktop\Indian(Sheet1)(in).csv"
result = pd.read_csv(file_path, encoding='latin1')

print(f"Data Preview (18 to 22 rows): \n{result[18:22+1]}")
print(f"Data Preview (from 10th row onward):\n{result[10:]}")
print(f"Data Preview (first 21 rows):\n{result[:20+1]}")