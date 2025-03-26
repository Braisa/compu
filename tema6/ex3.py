import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

w_0 = 10
w = 15
b, F = 1, 1
derivs = lambda t, x, y : np.array((y, -b*y -w_0**2 * x + F*np.cos(w*t)))

t0, x0, y0 = 0, 0, 1
deltas = (1e-2, 1e-3)
markers = (".", ",")

fig, ax = plt.subplots()
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

        t, x, y = t0, x0, y0
        #ax.plot(t, x, m, color = c, label = f"{l}, delta = {delta:.0e}")
        ax.plot(x, y, m, color = c, label = f"{l}, delta = {delta:.0e}")
        
        for _i in range(int(1/delta)):

            t += delta
            dx, dy = method(delta, derivs, t, pars = (x, y))
            x += dx
            y += dy

            #ax.plot(t, x, m, color = c)
            ax.plot(x, y, m, color = c)

ax.set_xlabel("x")
ax.set_ylabel("y")

#ax.set_xlim(left = t0, right = t0 + 1)

ax.legend(loc = "best", fontsize = "small")

fig.savefig("tema6/ex3.pdf", dpi = 300, bbox_inches = "tight")
