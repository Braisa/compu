import numpy as np
import matplotlib.pyplot as plt

# Brais Otero Lema
# Exercicio 9

N = 20
t_steps = 200
paint_step = 10
delta_t, delta_x = .05, .5
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

def implicit_diffusion_step(t, T, boundary, boundary_type):

    if boundary_type == "dirichlet":
        left, right = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        left, right = T[1] - delta_x * boundary[0](t), T[-2] - delta_x * boundary[-1](t)
    
    indep = np.hstack((left, T[1:-1], right))

    coeff = np.identity(N+1)
    coeff[1:-1,1:-1] += 2*s * np.identity(N-1)
    coeff[1:-1,0:N+1-2] += -(s + C/2) * np.identity(N-1)
    coeff[1:-1,2:] += (-s + C/2) * np.identity(N-1)

    T_new = np.linalg.inv(coeff) @ indep
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
        
        T = implicit_diffusion_step(t, T, boundary, boundary_type)

        if t % paint_step == 0:
            ax.plot(T, ls = "solid")

fig.savefig("tema8/ex9.pdf", dpi = 300, bbox_inches = "tight")
