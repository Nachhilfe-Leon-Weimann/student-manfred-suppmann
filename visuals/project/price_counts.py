import matplotlib.pyplot as plt

from data.reader import read

diamonds = read()

price_counts = dict[int, int]()
for d in diamonds:
    if d.price not in price_counts:
        price_counts[d.price] = 0
    price_counts[d.price] += 1

fig, ax = plt.subplots()
ax.set_title("Anzahl vs Preis")
ax.set_xlabel("Anzahl")
ax.set_ylabel("Preis")
plt.scatter(
    list(price_counts.values()),
    list(price_counts.keys()),
)
plt.show()
