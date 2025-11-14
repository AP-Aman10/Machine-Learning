import numpy as np

values = [2, 4, 10, 45, 96, 100, 81, 64, 47, 20]
result = np.array(values)

print(f"🔹 NumPy Array: {result}🔹")
print("-." * 50)

print(f"👉 All elements [ : ]               → {result[:]}")
print(f"👉 Array index 2 to 6 [2:7]         → {result[2:7]}")
print(f"👉 Array start to 6 [ :7]           → {result[:7]}")
print(f"👉 Array index 2 to end [2: ]       → {result[2:]}")
print(f"👉 Array 2 to 6, step 2 [2:7:2]     → {result[2:7:2]}")
print(f"👉 Array 7 to 2, step -2 [7:2:-2]   → {result[7:2:-2]}")