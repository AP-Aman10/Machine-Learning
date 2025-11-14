import numpy as np
from matplotlib import pyplot as plt

Value1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Value2 = [96, 20, 4, 10, 81, 47, 2, 100, 45, 64]

result = [Value1, Value2]

plt.boxplot(result, label=["Python", "C"], showmeans=True, sym="g+", boxprops=dict(color="red"))

# Title and labels
plt.title("Number of Value1 & Value2", fontsize=28, fontweight="bold")
plt.xlabel("Value1", fontsize=12)
plt.ylabel("Value2", fontsize=12)
plt.show()