import pandas as pd

file_path = r"C:\Users\Aman Patidar\Desktop\Indian(Sheet1)(in).csv"
result = pd.read_csv(file_path, encoding='latin1')

print(result.sort_index(axis=0, ascending=False))