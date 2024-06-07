import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

from sklearn.metrics import adjusted_rand_score

np.random.seed(0)

data = np.genfromtxt('impossible.csv', delimiter=',')[1:]

X, y = data[:, :-1], data[:, -1]

k = 7

net = Graph(n_classes=k)

net.fit(X, 200)

colors = plt.cm.tab10(np.arange(k))

guess = net.predict(X)

for i in range(k):
    plt.scatter(X[(y == i), 0], X[(y == i), 1], color='black', s=.5)
    plt.scatter(net.clusters[i][:, 0], net.clusters[i][:, 1], color=colors[i], label=f'Cluster {i}')

plt.show()

ari = adjusted_rand_score(y, guess)

print(f"Adjusted Rand Index: {ari}")