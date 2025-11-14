import numpy as np
Empty_List = []

num = int(input("Enter the number of elements you want in the array: "))
for i in range(num):
    Value = int(input(f"Enter element {i+1}: "))
    Empty_List.append(Value)
 
result = np.array(Empty_List)
print(f"Array: {result}")