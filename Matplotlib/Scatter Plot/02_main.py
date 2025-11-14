import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = np.array([89.6, 71.4, 89.4, 80.6, 59.6, 65.2])
ages = np.array([19, 16, 17, 18, 16, 18])

# Colors for each student
colors = np.array([100, 90, 80, 70, 60, 50])

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    ages,       # x-axis
    marks,      # y-axis
    s=200,      # marker size
    c=colors,   # color values
    marker="h",
    cmap='hsv',
    edgecolors='black'
)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label("Color Value", fontsize=12)

# Title and labels
plt.title("Student Marks vs Age", fontsize=28, fontweight="bold")
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)

plt.show()
