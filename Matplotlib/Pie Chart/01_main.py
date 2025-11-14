import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]

# Colors for each student
colors = ["red", "blue", "indigo", "magenta", "green", "yellow"]

# Explode the top scorer for emphasis
explode = [0.1 if mark == max(marks) else 0 for mark in marks]

# Corrected wedgeprops syntax
plt.pie(marks, labels=students, colors=colors, explode=explode, autopct="%0.1f%%", shadow=True, startangle=90, wedgeprops={"linewidth": 1.5, "edgecolor": "black"})
plt.title("Students' Marks Distribution", fontsize=14, fontweight="bold")
plt.legend(loc=2)

plt.show()
