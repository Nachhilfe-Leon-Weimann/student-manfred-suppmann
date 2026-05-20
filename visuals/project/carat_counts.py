import matplotlib.pyplot as plt

from data.reader import read

diamonds = read()

carat_counts = dict[float, int]()
for d in diamonds:
    if d.carat not in carat_counts:
        carat_counts[d.carat] = 0
    carat_counts[d.carat] += 1

fig, ax = plt.subplots()
ax.set_title("Anzahl vs Carat")
ax.set_xlabel("Anzahl")
ax.set_ylabel("Carat")
plt.scatter(
    list(carat_counts.values()),
    list(carat_counts.keys()),
)
plt.show()
