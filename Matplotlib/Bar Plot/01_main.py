import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]
 
# Style
# plt.figure(figsize=(8, 5))
color = ["Red", "Blue", "indigo", "Magenta", "Green", "Yellow"]
bars = plt.bar(students, marks, color=color, edgecolor="black", linewidth=1.2, alpha=0.9, label="Marks (%)")
plt.legend()

# Add title and labels
plt.title("Student Marks Comparison", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)

# Add grid for better readability
plt.grid(axis='y', linestyle='-.', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 1,
             f"{bar.get_height():.1f}%",
             ha='center', va='bottom', fontsize=10, fontweight='bold', color="#222")

# Improve layout
plt.tight_layout()
plt.show()
