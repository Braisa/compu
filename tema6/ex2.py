import numpy as np
import matplotlib.pyplot as plt

w_0 = 10
deriv_x = lambda y : y
deriv_y = lambda x : -w_0**2 * x

t0, x0, y0 = 0, 1, 1
delta = 1e-2

fig, ax = plt.subplots()
colors = ((1,.5,0,1), (.5,0,.5,.8), (0,0,1,.6))
labels = ("Euler", "R-K 2", "R-K 4")

def euler_step(f, par):
    return delta*f(par)

def rk2_step(f, par):
    return delta*f(par + delta/2*f(par))

def rk4_step(f, par):
    k1 = delta*f(par)
    k2 = delta*f(par + k1/2)
    k3 = delta*f(par + k2/2)
    k4 = delta*f(par + k3)
    return ((k1+k4)/2 + k2 + k3)/3

methods = (euler_step, rk2_step, rk4_step)

for _j, (method, c, l) in enumerate(zip(methods, colors, labels)):

    t, x, y = t0, x0, y0
    ax.plot(t, x, ".", color = c, label = l)
    
    for _i in range(int(1/delta)):

        t += delta
        dx = method(deriv_x, y)
        dy = method(deriv_y, x)
        x += dx
        y += dy

        ax.plot(t, x, ".", color = c)

ax.set_xlabel("t")
ax.set_ylabel("x")

ax.set_xlim(left = t0)

ax.legend(loc = "best")

fig.savefig("tema6/ex2.pdf", dpi = 300, bbox_inches = "tight")
