import numpy as np 
import matplotlib.pyplot as plt

N = 20
t_steps = 1000
delta_t, delta_x = .1, .5
alpha = 1

T0 = np.zeros(N+1)
T0[9:11] = 10

boundaries = (5, 3)

fig, ax = plt.subplots()

ax.plot(T0, ls = "solid")

def diffusion_step(T):
    T_new = np.zeros_like(T)
    T_new[0], T_new[-1] = boundaries
    T_new[1:-1] = T[1:-1] + alpha * delta_t / delta_x**2 * (T[:-2] - 2*T[1:-1] + T[2:])
    return T_new

T = T0

for t in range(t_steps):

    T = diffusion_step(T)

    if t % 10 == 0:
        ax.plot(T, ls = "solid")
        fig.savefig("tema7/exemplo_difusion.pdf", dpi = 300, bbox_inches = "tight")
        plt.pause(0.01)


ax.set_xlim(left = 0, right = N)

ax.set_xlabel("index")
ax.set_ylabel(r"$T$")

#fig.savefig("tema7/exemplo_difusion.pdf", dpi = 300, bbox_inches = "tight")
