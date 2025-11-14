import numpy as np
from matplotlib import pyplot as plt

students = ["Aman", "Preet", "Prabhat", "Subham", "Manav", "Kunal", "Mahak", "Henil", "Prince", "Lokesh"]
marks = [88.9, 64.9, 96.9, 79.6, 51.7, 79.1, 61.5, 56.4, 61.7, 52.1]

# 10 colors for 10 students
colors = {"red": "#FF0000", "blue": "#0000FF", "yellow": "#FFFF00", "green": "#008000", "orange": "#FFA500", "pink": "#FFC0CB", "purple": "#800080", "brown": "#A52A2A", "grey": "#808080", "cyan": "#00FFFF"}

plt.bar(students, marks, color=colors, edgecolor="black", linewidth=1.2, alpha=0.8)

# Set labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Plot of Students & Marks")

# Set y-axis range and ticks (x is categorical)
plt.ylim(0, 100)
plt.yticks(range(0, 101, 10))

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()