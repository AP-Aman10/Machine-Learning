import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]
ages = [19, 16, 17, 18, 16, 18]

# Colors for each student
colors = ["red", "blue", "green", "orange", "purple", "magenta"]

plt.figure(figsize=(8, 5))

# Scatter plot
plt.scatter(ages, marks, color=colors, s=200, marker="H", edgecolor='black')

# Add student names next to each point
for i, name in enumerate(students):
    plt.text(ages[i] + 0.1, marks[i] + 0.3, name, fontsize=9, fontweight='bold')

# Title and labels
plt.title("Student Marks vs Age (Scatter Plot)", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Age", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)

# Add grid
plt.grid(True, linestyle='-.', alpha=0.7)

# Improve layout
plt.tight_layout()
plt.show()
