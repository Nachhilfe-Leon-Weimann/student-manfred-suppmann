import matplotlib.pyplot as plt

from data.models import Clarity
from data.reader import read

diamonds = read()

clarity_counts = dict[Clarity, int]()
for d in diamonds:
    if d.clarity not in clarity_counts:  # noch kein passender Key im dict
        clarity_counts[d.clarity] = 0  # initialisiere den Key mit 0
    clarity_counts[d.clarity] += 1  # einfach hochzählen

fig, ax = plt.subplots()
ax.set_title("Anzahl vs Reinheit")
ax.set_xlabel("Reinheit")
ax.set_ylabel("Anzahl")
plt.bar(
    x=[c for c in clarity_counts.keys()],
    height=[c for c in clarity_counts.values()],
)
plt.show()
