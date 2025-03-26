import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

s, r, b = 3., 26.5, 1.
derivs = lambda t, x, y, z : np.array((s*(y - x),
                                       r*x - y - x*z,
                                       x*y - b*z))

T = 10
t0, x0, y0, z0 = 0, 0, 1, 0
deltas = (1e-2, 1e-3)
markers = (".", ",")

fig_x, ax_x = plt.subplots()
fig_y, ax_y = plt.subplots()
fig_z, ax_z = plt.subplots()
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

        t, x, y, z = t0, x0, y0, z0
        #ax.plot(t, x, m, color = c, label = f"{l}, delta = {delta:.0e}")
        ax_x.plot(t, x, m, color = c, label = f"{l}, delta = {delta:.0e}")
        ax_y.plot(t, y, m, color = c, label = f"{l}, delta = {delta:.0e}")
        ax_z.plot(t, z, m, color = c, label = f"{l}, delta = {delta:.0e}")
        
        for _i in range(T*int(1/delta)):

            t += delta
            dx, dy, dz = method(delta, derivs, t, pars = (x, y, z))
            x += dx
            y += dy
            z += dz

            #ax.plot(t, x, m, color = c)
            ax_x.plot(t, x, m, color = c)
            ax_y.plot(t, y, m, color = c)
            ax_z.plot(t, z, m, color = c)

ax_x.set_xlabel("t")
ax_y.set_xlabel("t")
ax_z.set_xlabel("t")

ax_x.set_ylabel("x")
ax_y.set_ylabel("y")
ax_z.set_ylabel("z")

ax_x.set_xlim(left = t0, right = t0 + T)
ax_y.set_xlim(left = t0, right = t0 + T)
ax_z.set_xlim(left = t0, right = t0 + T)

ax_x.legend(loc = "best", fontsize = "small")
ax_y.legend(loc = "best", fontsize = "small")
ax_z.legend(loc = "best", fontsize = "small")

fig_x.savefig("tema6/ex4_x.pdf", dpi = 300, bbox_inches = "tight")
fig_y.savefig("tema6/ex4_y.pdf", dpi = 300, bbox_inches = "tight")
fig_z.savefig("tema6/ex4_z.pdf", dpi = 300, bbox_inches = "tight")
