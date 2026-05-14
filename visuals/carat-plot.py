import matplotlib.pyplot as plt
import numpy as np

from data.models import Cut, Diamond
from data.reader import read

# fig, ax = plt.subplots()  # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()  # Show the figure.

# plt.boxplot([
#     [1, 2, 3, 2],
#     [4, 5, 6],
#     [7, 8, 9],
# ])  # Create a box plot from data in a list of lists.
# plt.show()  # Show the figure.


diamonds = read()

prices = list(map(lambda diamond: diamond.price, diamonds))
carats = list(map(lambda diamond: diamond.carat, diamonds))
cuts = list(map(lambda diamond: diamond.cut, diamonds))
clarity = list(map(lambda diamond: diamond.clarity, diamonds))
depth = list(map(lambda diamond: diamond.depth, diamonds))

fig, axs = plt.subplots(2, 2)

axs[0][0].scatter(
    prices,
    carats,
)

axs[0][1].scatter(
    prices,
    cuts,
)

axs[1][0].scatter(
    prices,
    clarity,
)

axs[1][1].scatter(
    prices,
    depth,
)

plt.show()

# print(np.array([d.carat for d in diamonds]))

# data = dict[Cut, list[Diamond]]()
# for d in diamonds:
#     if d.cut not in data:  # Ist der Cut als Key im Dictionary?
#         data[d.cut] = []  # Initialisiere den Key mit einem leeren Array
#     data[d.cut].append(d)  # Füge den Diamond zum Array des Cuts hinzu

# plt.scatter(
#     [d.carat for d in diamonds],
#     [d.price for d in diamonds],
# )
# plt.show()
