import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

N = 20
t_steps = 1000
delta_t, delta_x = .1, .5
alpha = 1

initial = np.zeros(N+1)
initial[9:11] = 20

boundary_dirichlet = (lambda t : 15, lambda t : 5)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)

def dirichlet_diffusion_step(t, T_curr, T_old, boundary):
    T_new = np.zeros_like(T_curr)

    T_new[1:-1] = 2/3 * (-.5*T_old[1:-1] + 2*T_curr[1:-1] + alpha * delta_t / delta_x**2 * (T_curr[:-2] - 2*T_curr[1:-1] + T_curr[2:]))
    
    T_new[0], T_new[-1] = boundary[0](t), boundary[-1](t)
    return T_new

def neumann_diffusion_step(t, T_curr, T_old, boundary):
    T_new = np.zeros_like(T_curr)

    T_new[1:-1] = 2/3 * (-.5*T_old[1:-1] + 2*T_curr[1:-1] + alpha * delta_t / delta_x**2 * (T_curr[:-2] - 2*T_curr[1:-1] + T_curr[2:]))
    
    T_new[0], T_new[-1] = T_new[1] - delta_x * boundary[0](t), T_new[-2] - delta_x * boundary[1](t)
    return T_new

methods = (dirichlet_diffusion_step, neumann_diffusion_step)

fig, axs = plt.subplots(1, 2)
titles = ("Dirichlet", "Fluxo nulo")

for _j, (boundary, method, ax, title) in enumerate(zip(boundaries, methods, np.ravel(axs), titles)):

    T, T_old = initial, initial
    ax.plot(T, ls = "solid")

    for t in range(t_steps):

        T_old = T.copy()
        T = method(t, T, T_old, boundary)

        if t % 10 == 0:
            ax.plot(T, ls = "solid")

    ax.set_xlim(left = 0, right = N)

    ax.set_xlabel("index")
    ax.set_ylabel(r"$T$")

    ax.set_title(title)

fig.savefig("tema7/ex2.pdf", dpi = 300, bbox_inches = "tight")
