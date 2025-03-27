import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

r, k = 1, 1
deriv = lambda p : r*p*(1-p/k)

T_max = 10

t0, p0 = 0, .01
delta0 = 1e-3

#crit_min, crit_max = .005, .01
crit_min, crit_max = .01, .05
delta_min, delta_max = 1e-4, 1e-2

fig, ax = plt.subplots()
ax_delta = ax.twinx()
c, c_delta = (1.,.5,0.,1.), (.8,0.,.8,1.)

def euler_step(x, delta):
    return delta*deriv(x)

t, p = t0, p0
delta = delta0
ax.plot(t, p, ".", color = c)
ax_delta.semilogy(t, delta, ".", color = c_delta, alpha = .5)

while t < T_max:

    dp = euler_step(p, delta)
    
    while delta == np.clip(delta, delta_min, delta_max):

        if np.abs(dp/p0) < crit_min:
            delta *= 2
        elif np.abs(dp/p0) > crit_max:
            delta /= 2
        else:
            break

        dp = euler_step(p, delta)
    
    delta = np.clip(delta, delta_min, delta_max)

    t += delta
    p += euler_step(p, delta)

    ax.plot(t, p, ".", color = c)
    ax_delta.semilogy(t, delta, ".", color = c_delta, alpha = .5)

ax.set_xlabel("t")

ax.set_ylabel("p", color = c)
ax_delta.set_ylabel("delta", color = c_delta)

ax.set_xlim(left = t0, right = T_max)

ax_delta.set_ylim(bottom = delta_min, top = delta_max)

ax.tick_params(axis = "y", labelcolor = c)
ax_delta.tick_params(axis = "y", labelcolor = c_delta)

ax_delta.yaxis.set_major_locator(plt.FixedLocator((delta_min, delta0, delta_max)))
ax_delta.yaxis.set_minor_locator(plt.AutoLocator())

fig.tight_layout()
fig.savefig("tema6/ex5.pdf", dpi = 300, bbox_inches = "tight")
