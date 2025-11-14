import numpy as np
from matplotlib import pyplot as plt

Value1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Value2 = [96, 20, 4, 10, 81, 47, 2, 100, 45, 64]

plt.stem(Value1, Value2, linefmt="b-.", markerfmt="rH", label="Number")
plt.legend()

# Title and labels
plt.title("Student Marks vs Age", fontsize=28, fontweight="bold")
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)
plt.show()