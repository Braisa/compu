import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema
# Exercicio 1

N = 20
t_steps = 1000
delta_t, delta_x = .1, .5
u = 1

C = u * delta_t / delta_x

initial = np.zeros(N+1)
initial[9:11] = 20

boundary_dirichlet = (lambda t : 0, lambda t : 0)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)
boundary_types = ("dirichlet", "neumann")

def diffusion_step(t, T_curr, boundary, boundary_type):
    T_new = np.zeros_like(T_curr)

    T_new[1:-1] = T_curr[1:-1] - C/2 * (T[2:] - T[:-2])

    if boundary_type == "dirichlet":
        T_new[0], T_new[-1] = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        T_new[0], T_new[-1] = T_new[1] - delta_x * boundary[0](t), T_new[-2] - delta_x * boundary[1](t)

    return T_new

fig, axs = plt.subplots(1, 2)
titles = ("Dirichlet", "Fluxo nulo")

for _j, (boundary, boundary_type, ax, title) in enumerate(zip(boundaries, boundary_types, np.ravel(axs), titles)):

    T = initial
    ax.plot(T, ls = "solid")

    ax.set_xlim(left = 0, right = N)

    ax.set_xlabel("index")
    ax.set_ylabel(r"$T$")

    ax.set_title(title)

    for t in range(t_steps):

        T = diffusion_step(t, T, boundary, boundary_type)

        if t % 10 == 0:
            ax.plot(T, ls = "solid")
            plt.pause(0.1)

#fig.savefig("tema8/ex1.pdf", dpi = 300, bbox_inches = "tight")
