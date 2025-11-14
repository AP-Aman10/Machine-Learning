import numpy as np
from matplotlib import pyplot as plt

Value1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Value2 = [96, 20, 4, 10, 81, 47, 2, 100, 45, 64]

plt.boxplot(Value2, Value1, patch_artist=True, showmeans=True, boxprops=dict(color="black"))

# Title and labels
plt.title("Number of Value1 & Value2", fontsize=28, fontweight="bold")
plt.xlabel("Value1", fontsize=12)
plt.ylabel("Value2", fontsize=12)
plt.show()