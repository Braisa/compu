import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema

N = 20
t_steps = 1000
delta_t, delta_x = .1, .5
alpha = 1

s = alpha * delta_t / delta_x**2

initial = np.zeros(N+1)
initial[9:11] = 20

boundary_dirichlet = (lambda t : 15, lambda t : 5)
boundary_neumann = (lambda t : 0, lambda t : 0)
boundaries = (boundary_dirichlet, boundary_neumann)
boundary_types = ("dirichlet", "neumann")

def implicit_diffusion_step(t, T, boundary, boundary_type):

    if boundary_type == "dirichlet":
        left, right = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        left, right = T[1] - delta_x * boundary[0](t), T[-2] - delta_x * boundary[-1](t)
    
    middle = s/2 * T[:-2] + (1-s) * T[1:-1] + s/2 * T[2:]
    indep = np.hstack((left, middle, right))

    coeff = np.identity(N+1)
    coeff[1:-1,1:-1] += s * np.identity(N-1)
    coeff[1:-1,0:N+1-2] -= s/2 * np.identity(N-1)
    coeff[1:-1,2:] -= s/2 * np.identity(N-1)

    T_new = np.linalg.inv(coeff) @ indep
    return T_new

fig, axs = plt.subplots(1, 2)
titles = ("Dirichlet", "Fluxo nulo")

for _j, (boundary, boundary_type, ax, title) in enumerate(zip(boundaries, boundary_types, np.ravel(axs), titles)):

    T, T_old = initial, initial
    ax.plot(T, ls = "solid")

    for t in range(t_steps):

        T_old = T.copy()
        T = implicit_diffusion_step(t, T, boundary, boundary_type)

        if t % 10 == 0:
            ax.plot(T, ls = "solid")

    ax.set_xlim(left = 0, right = N)

    ax.set_xlabel("index")
    ax.set_ylabel(r"$T$")

    ax.set_title(title)

fig.savefig("tema7/ex6.pdf", dpi = 300, bbox_inches = "tight")
