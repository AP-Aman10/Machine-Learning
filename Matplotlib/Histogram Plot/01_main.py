import numpy as np
from matplotlib import pyplot as plt

Value = [61, 12, 93, 99, 18, 2, 16, 98, 49, 8, 48, 43, 92, 54, 63, 11, 46, 36, 60, 15, 26, 51, 97, 31, 40, 70, 4, 35, 87, 39, 28, 24, 100, 73, 91, 86, 76, 6, 13, 94, 65, 52, 41, 37, 71, 75, 90, 82, 44, 32]

plt.figure(figsize=(10,6))
plt.hist(Value, bins=10, color="#ff0000", edgecolor="black", rwidth=0.8, log=False)

plt.title("Distribution of Values", fontsize=18, fontweight="bold", color="#333")
plt.xlabel("Value", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='-.', alpha=0.7)
plt.xticks(range(0, 110, 10))

plt.show()
