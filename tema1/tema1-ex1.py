import numpy as np
import matplotlib.pyplot as plt

function = lambda x : x**2 - 3*x + np.exp(x) - 2

x_int = np.linspace(-2, 4, 20, endpoint=False)

def check_root(func, x_left, x_right):
    return func(x_left) * func(x_right) < 0

roots = np.array(())

for i, x in enumerate(x_int[:-1]):
    # Root found
    if check_root(function, x, x_int[i+1]):
        roots = np.append(roots, np.array((x, x_int[i+1])))

roots = np.reshape(roots, (int(np.size(roots)/2), 2))

for r, root in enumerate(roots):
    print(f"A raíz {r+1} atópase no subintervalo ({root[0]:.1f},{root[1]:.1f}).")

# Exercicio 2

fig, ax = plt.subplots()

x_lin = np.linspace(-2, 4, 1000)

ax.plot(x_lin, np.zeros_like(x_lin), ls = "solid", color = "tab:gray")
ax.plot(x_lin, function(x_lin), ls = "solid", color = "tab:orange")

ax.set_xlabel("x")
ax.set_ylabel("f(x)")

ax.set_title(r"$f(x) = x^2 - 3x + e^x - 2$")

ax.set_xlim(left = -2, right = 4)
ax.set_ylim(bottom = 2*np.min(function(x_lin)), top = 1.05*np.max(function(x_lin)))

fig.savefig("tema1-ex2.pdf", dpi = 300, bbox_inches = "tight")
