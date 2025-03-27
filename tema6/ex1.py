import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

r, k = 1, 1
deriv = lambda p : r*p*(1-p/k)

T = 3

t0, p0 = 0, 10
delta = 1e-2

fig, ax = plt.subplots()
colors = ((1,.5,0,1), (.5,0,.5,.8), (0,0,1,.6))
labels = ("Euler", "R-K 2", "R-K 4")

def euler_step(x):
    return x + delta*deriv(x)

def rk2_step(x):
    return x + delta*deriv(x + delta/2*deriv(x))

def rk4_step(x):
    k1 = delta*deriv(x)
    k2 = delta*deriv(x + k1/2)
    k3 = delta*deriv(x + k2/2)
    k4 = delta*deriv(x + k3)
    return x + ((k1+k4)/2 + k2 + k3)/3

methods = (euler_step, rk2_step, rk4_step)

for _j, (method, c, l) in enumerate(zip(methods, colors, labels)):

    t, p = t0, p0
    ax.plot(t, p, ".", color = c, label = l)
    
    for _i in range(T*int(1/delta)):

        t += delta
        p = method(p)

        ax.plot(t, p, ".", color = c)

ax.set_xlabel("t")
ax.set_ylabel("p")

ax.set_xlim(left = t0, right = t0 + T)

ax.legend(loc = "best")

fig.savefig("tema6/ex1.pdf", dpi = 300, bbox_inches = "tight")
