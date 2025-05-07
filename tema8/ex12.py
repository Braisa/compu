import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.cm import plasma
import cmasher as cmr

# Brais Otero Lema
# Exercicio 12

N = 20
t_steps = 200
paint_step = 10
delta_t, delta_x = .05, .5
u = 1
alpha_x, alpha_y = 1, 1

s_x, s_y = alpha_x * delta_t / delta_x**2, alpha_y * delta_t / delta_x**2
C = u * delta_t / delta_x

initial = np.zeros((N+1,N+1))
initial[9:11,9:11] = 5

# Bottom, Right, Top, Left
boundary_strips = (10*np.ones(N-1),np.zeros(N-1),np.zeros(N-1),10*np.ones(N-1))
# Bottom left, Bottom right, Top right, Top left
boundary_corners = (10,10,0,10)

def diffusion_step(t, T, boundary_strips, boundary_corners):

    T_new = np.zeros_like(T)

    T_new[0,0], T_new[-1,0], T_new[-1,-1], T_new[0,-1] = boundary_corners
    T_new[1:-1,0], T_new[-1,1:-1], T_new[1:-1,-1], T_new[0,1:-1] = boundary_strips

    T_new[1:-1,1:-1] = (1-2*(s_x+s_y)) * T[1:-1,1:-1] + s_x * (T[:-2,1:-1] + T[2:,1:-1]) + s_y * (T[1:-1,:-2] + T[1:-1,2:])

    return T_new

sub_plasma = cmr.get_sub_cmap(plasma, .2, .9)
colors = sub_plasma(np.linspace(0, 1, 11))

bounds = np.arange(12)
norm = mpl.colors.BoundaryNorm(bounds, sub_plasma.N)

fig, ax = plt.subplots(figsize = (7,6))

cbar = fig.colorbar(mpl.cm.ScalarMappable(norm = norm, cmap = sub_plasma),
                    ax = ax, orientation = "vertical", label = r"$T$")
cbar.ax.set_yticks(.5 + np.arange(11))
cbar.ax.set_yticklabels(np.arange(11))
cbar.ax.minorticks_off()

T = initial
ax.pcolor(T, cmap = sub_plasma)

ax.set_xlim(left = 0, right = N)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

for t in range(t_steps):
    
    T = diffusion_step(t, T, boundary_strips, boundary_corners)

    if t % paint_step == 0:
        ax.pcolor(T, cmap = sub_plasma)

fig.savefig("tema8/ex12.pdf", dpi = 300, bbox_inches = "tight")
