import numpy as np
Empty_List = []

num = int(input("Enter the number to print the table: "))
for i in range(1, 10+1):
    Value = num * i
    Empty_List.append(Value)
    
result = np.array(Empty_List)
print(f"Table of {num}: {result}")