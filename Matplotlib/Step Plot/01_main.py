import numpy as np
from matplotlib import pyplot as plt

Value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [96, 20, 4, 10, 81, 47, 2, 100, 45, 64]

plt.step(Value, result, color="Black", marker="H", mfc="Red", label="Value")
plt.legend()
plt.title("Value & result Step Plot", fontsize=16, fontweight="bold", color="#000000")
plt.xlabel("Value", fontsize=12)
plt.ylabel("result", fontsize=12)

plt.show()