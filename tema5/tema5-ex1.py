import numpy as np
import matplotlib.pyplot as plt
import random as rd

length = 600
possible_steps = [1,-1]
steps = rd.sample(possible_steps, counts = (length, length), k = length)

fig, ax = plt.subplots()

ax.set_xlim(left = 0, right = length)

ax.plot(range(length), np.cumsum(steps), ls = "solid", color = "tab:orange")

ax.set_xlabel("Pasos")
ax.set_ylabel(r"$y$")

fig.savefig("tema5/tema5-ex1.pdf", dpi = 300, bbox_inches = "tight")
