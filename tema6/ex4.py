import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

s, r, b = 3., 26.5, 1.
derivs = lambda t, x, y, z : np.array((s*(y - x),
                                       r*x - y - x*z,
                                       x*y - b*z))

T = 5
t0, coords0 = 0, (0,1,0)
deltas = (1e-2, 1e-3)

fig = plt.figure()
ax_euler = fig.add_subplot(1, 3, 1, projection = "3d")
ax_rk2 = fig.add_subplot(1, 3, 2, projection = "3d")
ax_rk4 = fig.add_subplot(1, 3, 3, projection = "3d")
axs = (ax_euler, ax_rk2, ax_rk4)

colors = ((1,.5,0,1), (.5,0,.5,.8), (0,0,1,.6))
titles = ("Euler", "R-K 2", "R-K 4")

def euler_step(delta, funcs, t, pars):
    return delta*funcs(t, *pars)

def rk2_step(delta, funcs, t, pars):
    k1s = delta * funcs(t, *pars)
    k2s = delta * funcs(t + delta/2, *pars + k1s/2)
    return k2s

def rk4_step(delta, funcs, t, pars):
    k1s = delta * funcs(t, *pars)
    k2s = delta * funcs(t + delta/2, *pars + k1s/2)
    k3s = delta * funcs(t + delta/2, *pars + k2s/2)
    k4s = delta * funcs(t + delta, *pars + k3s)
    return ((k1s+k4s)/2 + k2s + k3s)/3

methods = (euler_step, rk2_step, rk4_step)

for _k, (ax, title, method) in enumerate(zip(axs, titles, methods)):

    for _j, (delta, c) in enumerate(zip(deltas, colors)):

        store_x, store_y, store_z = np.array((coords0[0])), np.array((coords0[1])), np.array((coords0[2]))

        t, coords = t0, coords0
        ax.scatter(coords[0], coords[1], coords[2], ",", color = c, label = f"delta = {delta:.0e}")
        
        for _i in range(T*int(1/delta)):

            dcoords = method(delta, derivs, t, pars = coords)
            t += delta
            coords += dcoords

            store_x = np.append(store_x, coords[0])
            store_y = np.append(store_y, coords[1])
            store_z = np.append(store_z, coords[2])

        ax.scatter(store_x, store_y, store_z, ",", color = c)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.legend(loc = "best", fontsize = "small")

    ax.set_title(title)

#fig.savefig(f"tema6/ex4_3d.pdf", dpi = 300, bbox_inches = "tight")
plt.show()
