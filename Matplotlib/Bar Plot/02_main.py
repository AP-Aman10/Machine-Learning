import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]
ages = [19, 16, 17, 18, 16, 18]

# X-axis positions
x = np.arange(len(students))
width = 0.35  # width of bars

plt.figure(figsize=(8, 5))

# Plot bars
bar1 = plt.bar(x - width/2, marks, width, color="red", edgecolor="black", label="Marks (%)")
bar2 = plt.bar(x + width/2, ages, width, color="magenta", edgecolor="black", label="Age")

# Title and labels
plt.title("Student Marks & Age Comparison", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.xticks(x, students)

# Set Y-axis ticks manually (10, 20, 30, ...)
plt.yticks(np.arange(0, 101, 10))   # from 0 to 100 in steps of 10

# Grid
plt.grid(axis='y', linestyle='-.', alpha=0.7)

# Add value labels
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                 f"{height:.1f}", ha='center', va='bottom', fontsize=9, fontweight='bold')

add_labels(bar1)
add_labels(bar2)

# Legend and layout
plt.legend()
plt.tight_layout()
plt.show()

