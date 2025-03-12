import numpy as np
import random as rd

R = 1.5
radio = lambda x, y : np.sqrt(x**2 + y**2)
condition = lambda x, y : radio(x, y) < R
Ns = 10 ** np.array(range(2,9))

print(" "*8 + "N" + " "*8 + "I" + " "*9 + "Erro")

for N in Ns:
    points_x = np.fromiter((rd.uniform(-R,R) for k in range(N)), dtype = float)
    points_y = np.fromiter((rd.uniform(-R,R) for k in range(N)), dtype = float)
    inside_count = np.sum(condition(points_x, points_y))

    integral = (2*R)**2 * inside_count / N
    error_est = (2*R)**2 * np.sqrt(inside_count * (1 - inside_count/N)) / N

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e}")
