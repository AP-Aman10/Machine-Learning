import pandas as pd

file_path = r"C:\Users\Aman Patidar\Desktop\Indian(Sheet1)(in).csv"
result = pd.read_csv(file_path, encoding='latin1')

print(f"File path Contents: \n{result.to_numpy()}")