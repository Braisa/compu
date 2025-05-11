import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema
# Exercicio 8

N = 20
t_steps = 200
paint_step = 10
delta_t, delta_x = .05, .5 # Debe verificarse C <= 1
u = 1
alpha = 1

s = alpha * delta_t / delta_x**2
C = u * delta_t / delta_x

initial = np.zeros(N+1)
initial[1:3] = 20

boundary_dirichlet = (lambda t : 0, lambda t : 0)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)
boundary_types = ("dirichlet", "neumann")   

def diffusion_step(t, T_curr, T_old, boundary, boundary_type):
    T_new = np.zeros_like(T_curr)

    T_new[1:-1] = ((1-2*s)*T_old[1:-1] - C*T_curr[1:-1] + 2*s*(T_curr[:-2] + T_curr[2:]))/(1+2*s)

    if boundary_type == "dirichlet":
        T_new[0], T_new[-1] = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        T_new[0], T_new[-1] = T_new[1] - delta_x * boundary[0](t), T_new[-2] - delta_x * boundary[1](t)

    # Promedio para mesturar información
    T_new[1:-1] = .5 * (T_new[1:-1] + T[1:-1]).copy()

    return T_new

fig, axs = plt.subplots(1, 2)
titles = ("Dirichlet", "Fluxo nulo")

for _j, (boundary, boundary_type, ax, title) in enumerate(zip(boundaries, boundary_types, np.ravel(axs), titles)):

    T, T_old = initial, initial
    ax.plot(T, ls = "solid")

    ax.set_xlim(left = 0, right = N)

    ax.set_xlabel("index")
    ax.set_ylabel(r"$T$")

    ax.set_title(title)

    for t in range(t_steps):
        
        T_old = T.copy()
        T = diffusion_step(t, T, T_old, boundary, boundary_type)

        if t % paint_step == 0:
            ax.plot(T, ls = "solid")
            plt.pause(0.1)

#fig.savefig("tema8/ex8.pdf", dpi = 300, bbox_inches = "tight")
