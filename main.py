import numpy as np
import matplotlib.pyplot as plt

# data = random.random((10, 10))
face = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

ghost = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

pacman = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maps = [face, ghost, pacman]

for map in maps:

    fig, ax = plt.subplots()
    img = ax.matshow(map, interpolation='nearest', cmap='hot')

    ax.set_xticks(np.arange(10), minor=True)
    ax.set_xticklabels(np.arange(10), minor=True)

    ax.set_yticks(np.arange(10), minor=True)
    ax.set_yticklabels(np.arange(10), minor=True)

    plt.xticks(np.arange(11)-0.5,[])
    plt.yticks(np.arange(11)-0.5,[])

    plt.grid(True, linestyle='dotted', linewidth=1, color='k')
    plt.plot()
    # plt.savefig("test.png", bbox_inches='tight')
    plt.show()
