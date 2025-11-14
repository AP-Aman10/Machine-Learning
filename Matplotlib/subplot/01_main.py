import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]

# Short names for bar chart
short_names = ["Am", "Pr", "Sh", "Pc", "Ku", "Mh"]

# Markers and colors
markers = ["H", "p", "h", "^", "D", "d"]
colors = ["#FA5757", "#4ECDC4", "#556270", "#C44DFF", "#45B7D1", "#F7B733"]

# Figure setup
plt.figure(figsize=(12, 9))
plt.suptitle("Students' Marks Visualization", fontsize=18, fontweight="bold", color="#333")

# --- Pie Chart ---
plt.subplot(2, 2, 1)
plt.pie(
    marks,
    labels=students,
    colors=colors,
    autopct="%0.1f%%",
    shadow=True,
    startangle=90,
    wedgeprops={"linewidth": 1.2, "edgecolor": "black"}
)
plt.title("Marks Distribution (Pie Chart)", fontsize=13, fontweight="bold")

# --- Bar Chart ---
plt.subplot(2, 2, 2)
plt.bar(short_names, marks, color=colors, edgecolor="black", linewidth=1.2)
plt.title("Marks Comparison (Bar Chart)", fontsize=13, fontweight="bold")
plt.xlabel("Students", fontsize=11)
plt.ylabel("Marks", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# --- Scatter Plot ---
plt.subplot(2, 2, 3)
for i in range(len(students)):
    plt.scatter(students[i], marks[i], color=colors[i], s=200, marker=markers[i], edgecolor='black', linewidth=1.2)

plt.title("Individual Marks (Scatter Plot)", fontsize=13, fontweight="bold")
plt.xlabel("Students", fontsize=11)
plt.ylabel("Marks", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)

# --- Stem Plot ---
plt.subplot(2, 2, 4)
markerline, stemlines, baseline = plt.stem(students, marks, linefmt="b-.", markerfmt="rH", basefmt="k-")
plt.setp(markerline, markersize=10, markeredgecolor="black", markerfacecolor="red")
plt.title("Marks Visualization (Stem Plot)", fontsize=13, fontweight="bold")
plt.xlabel("Students", fontsize=11)
plt.ylabel("Marks", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Adjust layout and spacing
plt.tight_layout(pad=3.0, rect=[0, 0, 1, 0.96])

# Show all plots
plt.show()
