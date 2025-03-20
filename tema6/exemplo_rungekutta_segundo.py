import numpy as np
import matplotlib.pyplot as plt
import time

origin = time.time()

deriv = lambda x : np.sin(x)
t0, x0 = 0, 1
deltas = (1e-3, 1e-2, 1e-1)

fig, ax = plt.subplots()
colors = ("tab:orange", "tab:purple", "tab:blue")

for k, (delta, c) in enumerate(zip(deltas, colors)):
    
    t, x = t0, x0
    ax.plot(t, x, ".", color = c, label = f"{delta}")
    
    for i in range(int(1/delta)):

        t += delta
        x += delta*deriv(x + delta/2*deriv(x))

        ax.plot(t, x, ".", color = c)

ax.set_xlabel("t")
ax.set_ylabel("x")

ax.set_xlim(left = t0)

ax.legend(loc = "best")

fig.savefig("tema6/exemplo_rungekutta_segundo.pdf", dpi = 300, bbox_inches = "tight")

print(f"Tempo de execución : {time.time() - origin:.2f}")
