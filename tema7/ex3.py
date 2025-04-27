import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema
# Exercicio 3

N = 20
t_steps = 1000
delta_t, delta_x = .01, .5
alpha = 1

initial = np.zeros(N+1)
initial[9:11] = 20

boundary_dirichlet = (lambda t : 15, lambda t : 5)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)
boundary_types = ("dirichlet", "neumann")

def diffusion_step(t, T, boundary, boundary_type):
    T_new = np.zeros_like(T)

    T_new[2:-2] = T[2:-2] + alpha * delta_t / delta_x**2 * (-1/12*(T[4:] + T[:-4]) + 4/3*(T[3:-1] + T[1:-3]) - 5/2*T[2:-2])
    
    if boundary_type == "dirichlet":
        T_new[1], T_new[-2] = boundary[0](t), boundary[-1](t)
        T_new[0], T_new[-1] = T_new[1], T_new[-2]
    elif boundary_type == "neumann":
        T_new[1], T_new[-2] = T_new[2] - delta_x * boundary[0](t), T_new[-3] - delta_x * boundary[1](t)
        T_new[0], T_new[-1] = T_new[1], T_new[-2]
    
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
            plt.pause(1/(1+t))

#fig.savefig("tema7/ex3.pdf", dpi = 300, bbox_inches = "tight")
