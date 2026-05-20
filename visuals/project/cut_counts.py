import matplotlib.pyplot as plt

from data.models import Cut
from data.reader import read

diamonds = read()

cut_counts = dict[Cut, int]()
for d in diamonds:
    if d.cut not in cut_counts:
        cut_counts[d.cut] = 0
    cut_counts[d.cut] += 1

fig, ax = plt.subplots()
ax.set_title("Anzahl vs Cut")
ax.set_xlabel("Anzahl")
ax.set_ylabel("Cut")
plt.bar(
    x=[c for c in cut_counts.keys()],
    height=[c for c in cut_counts.values()],
)
plt.show()
