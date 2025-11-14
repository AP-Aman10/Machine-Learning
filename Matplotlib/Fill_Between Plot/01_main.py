import numpy as np
from matplotlib import pyplot as plt

Value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = np.array([96, 20, 4, 10, 81, 47, 2, 100, 45, 64])

plt.plot(Value, result, color="black", marker='o')

# Select the region where x is between 2 and 4
mask = (Value >= 2) & (Value <= 4)

# Fill between the curve and the x-axis for that region
plt.fill_between(Value[mask], result[mask], color='red')

plt.title("Value & Result", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Value", fontsize=12)
plt.ylabel("Result", fontsize=12)

plt.show()
