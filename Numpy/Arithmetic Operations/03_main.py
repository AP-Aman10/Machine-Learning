import numpy as np
np.set_printoptions(precision=2)

Value = [47, 2, 81, 4, 100, 64, 20, 10, 94, 45]
result = np.array(Value)

print(f"Array: {result}")
print()
print(f"Minimum Value: {np.min(result)} =><= Index: {np.argmin(result)}")
print(f"Maximum Value: {np.max(result)} =><= Index: {np.argmax(result)}")
print(f"Square Root: {np.sqrt(result)}")
print(f"Sin: {np.sin(result)}")
print(f"Cos: {np.cos(result)}")
print(f"Standard Deviation: {np.std(result)}")
print(f"Mean: {np.mean(result)}")
print(f"Median: {np.median(result)}")