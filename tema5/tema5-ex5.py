import numpy as np
import random as rd
import time

R = 1.66
radio = lambda x, y, z : np.sqrt(x**2 + y**2 + z**2)
condition = lambda x, y, z : radio(x, y, z) < R
Ns = 10 ** np.array(range(2,9))

print(" "*8 + "N" + " "*8 + "I" + " "*9 + "Erro" + "    Tempo")

origin = time.time()

for N in Ns:
    points_x = np.fromiter((rd.uniform(-R,R) for k in range(N)), dtype = float)
    points_y = np.fromiter((rd.uniform(-R,R) for k in range(N)), dtype = float)
    points_z = np.fromiter((rd.uniform(-R,R) for k in range(N)), dtype = float)
    inside_count = np.sum(condition(points_x, points_y, points_z))

    integral = (2*R)**3 * inside_count / N
    error_est = (2*R)**3 * np.sqrt(inside_count * (1 - inside_count/N)) / N

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e} {time.time() - origin:.3f}")
