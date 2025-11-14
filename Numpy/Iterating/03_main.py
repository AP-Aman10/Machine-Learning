import numpy as np

Value = [[4, 2, 10, 45, 96], [20, 81, 64, 47, 100]]
result = np.array(Value)

print(f"Array: \n{result}")
print()
for R in np.nditer(result):
    print(f"Index: {R}")