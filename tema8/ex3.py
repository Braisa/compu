import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import plasma
import cmasher as cmr

# Brais Otero Lema

N = 20
t_steps = 100
paint_step = 10
delta_t, delta_x = .1, .5
u = 1

C = u * delta_t / delta_x

initial = np.zeros(N+1)
initial[9:11] = 20

boundary_dirichlet = (lambda t : 0, lambda t : 0)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)
boundary_types = ("dirichlet", "neumann")

def diffusion_step(t, T_curr, T_old, boundary, boundary_type):
    T_new = np.zeros_like(T_curr)

    T_new[1:-1] = T_old[1:-1] - C * (T_curr[2:] - T_curr[:-2])

    if boundary_type == "dirichlet":
        T_new[0], T_new[-1] = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        T_new[0], T_new[-1] = T_new[1] - delta_x * boundary[0](t), T_new[-2] - delta_x * boundary[1](t)

    # Promedio para mesturar información
    T_new[1:-1] = .5 * (T_new[1:-1] + T[1:-1]).copy()

    return T_new

fig, axs = plt.subplots(1, 2)
titles = ("Dirichlet", "Fluxo nulo")
sub_plasma = cmr.get_sub_cmap(plasma, .2, .9)
colors = sub_plasma(np.linspace(0, 1, int(t_steps/paint_step)))

for _j, (boundary, boundary_type, ax, title) in enumerate(zip(boundaries, boundary_types, np.ravel(axs), titles)):

    T, T_old = initial, initial
    ax.plot(T, ls = "solid", color = colors[0])

    for t in range(t_steps):
        
        T_old = T
        T = diffusion_step(t, T, T_old, boundary, boundary_type)

        if t % paint_step == 0:
            ax.plot(T, ls = "solid", color = colors[int(t/paint_step)])

    ax.set_xlim(left = 0, right = N)

    ax.set_xlabel("index")
    ax.set_ylabel(r"$T$")

    ax.set_title(title)

fig.savefig("tema8/ex3.pdf", dpi = 300, bbox_inches = "tight")
