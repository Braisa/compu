import numpy as np 
import matplotlib.pyplot as plt

# Brais Otero Lema
# Exercicio 1

N = 20
t_steps = 1000
delta_t, delta_x = .1, .5
alpha = 1

T0 = np.zeros(N+1)
T0[9:11] = 10

T1 = 10 * np.sin(np.arange(N+1))

initial_conds = (T0, T1, T0, T0)

b1 = (lambda t : 5, lambda t : 3)
b2 = (lambda t : 5, lambda t : np.sin(t/2))
neu = (lambda t : 0, lambda t : 0)

boundaries = (b1, b1, b2, neu)
boundary_types = ("dirichlet", "dirichlet", "dirichlet", "neumann")

fig, axs = plt.subplots(2, 2)
titles = ("(a)", "(b)", "(c)", "(d)")

def diffusion_step(t, T, boundary, boundary_type):
    T_new = np.zeros_like(T)
    
    T_new[1:-1] = T[1:-1] + alpha * delta_t / delta_x**2 * (T[:-2] - 2*T[1:-1] + T[2:])
    
    if boundary_type == "dirichlet":
        T_new[0], T_new[-1] = boundary[0](t), boundary[-1](t)
    elif boundary_type == "neumann":
        T_new[0], T_new[-1] = T_new[1] - delta_x * boundary[0](t), T_new[-2] - delta_x * boundary[1](t)
    
    return T_new

for _j, (ax, title, initial, boundary, boundary_type) in enumerate(zip(np.ravel(axs), titles, initial_conds, boundaries, boundary_types)):

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

fig.tight_layout()
#fig.savefig("tema7/ex1.pdf", dpi = 300, bbox_inches = "tight")
