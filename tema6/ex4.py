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
markers = (".", ",")

fig_x, ax_x = plt.subplots()
fig_y, ax_y = plt.subplots()
fig_z, ax_z = plt.subplots()
figs, axs = (fig_x,fig_y,fig_z), (ax_x,ax_y,ax_z)
names = ("x","y","z")

colors = ((1,.5,0,1), (.5,0,.5,.8), (0,0,1,.6))
labels = ("Euler", "R-K 2", "R-K 4")

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

for _z, (delta, m) in enumerate(zip(deltas, markers)):

    for _j, (method, c, l) in enumerate(zip(methods, colors, labels)):

        t, coords = t0, coords0
        #ax.plot(t, x, m, color = c, label = f"{l}, delta = {delta:.0e}")

        for _i, (ax, coord) in enumerate(zip(axs, coords)):
            ax.plot(t, coord, m, color = c, label = f"{l}, delta = {delta:.0e}")
        
        for _i in range(T*int(1/delta)):

            t += delta
            dcoords = method(delta, derivs, t, pars = coords)
            coords += dcoords

            for _k, (ax, coord) in enumerate(zip(axs, coords)):
                ax.plot(t, coord, m, color = c)

for _i, (fig, ax, name) in enumerate(zip(figs, axs, names)):

    ax.set_xlabel("t")
    ax.set_ylabel(name)

    ax.set_xlim(left = t0, right = t0 + T)

    ax.legend(loc = "best", fontsize = "small")

    fig.savefig(f"tema6/ex4_{name}.pdf", dpi = 300, bbox_inches = "tight")
