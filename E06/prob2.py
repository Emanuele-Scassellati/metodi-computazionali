import numpy as np
import matplotlib.pyplot as plt
from random_walk import random_walk

l = 1.0
N = 10000000

x, y = random_walk(l, N)

plt.figure(figsize=(6, 6))
plt.plot(x, y, alpha=0.8)
plt.title("Random Walk 2D")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

#pannello della traiettoria
ax1.plot(x, y, alpha=0.8, color='royalblue')
ax1.set_title("Traiettoria 2D")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.axis("equal")
ax1.grid(True)

#pannello quadrato della distanza 
passi = np.arange(1, N + 1)
r = x**2 + y**2
ax2.plot(passi, r, alpha=0.8, color='purple')
ax2.set_title("Quadrato della Distanza ($r^2$) vs Passi")
ax2.set_xlabel("Numero di Passi")
ax2.set_ylabel("$r^2$")
ax2.grid(True)

plt.tight_layout()
plt.show()