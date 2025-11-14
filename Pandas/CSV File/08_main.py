import pandas as pd

file_path = r"C:\Users\Aman Patidar\Desktop\Indian(Sheet1)(in).csv"
result = pd.read_csv(file_path, encoding='latin1')

updated_result1 = result.replace({
    "Gujarat": "Rajasthan",
    "Andhra Pradesh": "Maharashtra"
})

print("== Updated DataFrame: Gujarat → Rajasthan ==")
print("== Updated DataFrame: Andhra Pradesh → Maharashtra ==\n")
print(f"{updated_result1}")