import numpy as np
from matplotlib import pyplot as plt

# Data
Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Area1 = [96, 20, 4, 10, 81, 47, 2, 100, 45, 64]
Area2 = [12, 85, 57, 64, 29, 90, 71, 56, 3, 78]
Area3 = [22, 49, 61, 7, 94, 68, 33, 72, 80, 11]
Area4 = [50, 88, 26, 70, 55, 63, 39, 81, 47, 2]

# Consistent labels and colors
labels = ["Area 1", "Area 2", "Area 3", "Area 4"]
colors = ["blue", "magenta", "indigo", "Red"]  # magenta, indigo, cyan, red-orange

# Plot
plt.figure(figsize=(10, 6))
plt.stackplot(Num, Area1, Area2, Area3, Area4, labels=labels, colors=colors, alpha=0.85, edgecolor="black", linewidth=0.5)

# Enhancements
plt.legend(title="Areas", loc="upper left", fontsize=10)
plt.title("Student Marks Comparison", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Student Number", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)
plt.grid(alpha=0.3, linestyle="--")
plt.tight_layout()

# Show
plt.show()