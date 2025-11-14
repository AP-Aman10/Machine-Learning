import numpy as np
from matplotlib import pyplot as plt

# Data
students = ["Aman", "Preet", "Subham", "Prince", "Kunal", "Mahak"]
marks = [89.6, 71.4, 89.4, 80.6, 59.6, 65.2]
colors = ["red", "blue", "indigo", "magenta", "green", "yellow"]

# Explode the top scorer
explode = [0.1 if mark == max(marks) else 0 for mark in marks]

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    marks,
    labels=students,
    colors=colors,
    explode=explode,
    autopct="%0.1f%%",
    shadow=True,
    startangle=90
)

# Draw white circle in the center to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Students' Marks Distribution", fontsize=14)
plt.show()
