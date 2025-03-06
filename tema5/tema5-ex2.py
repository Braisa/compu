import numpy as np
import random as rd

func = lambda x : (1-x**2)**1.5
left, right = 0, 1
Ns = 10 ** np.array(range(2,9))

print(" "*8 + "N" + " "*8 + "I" + " "*9 + "Erro")

for N in Ns:
    points_x = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    points_y = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    inside_count = np.count_nonzero(points_y < func(points_x))

    integral = (right - left)**2 * inside_count / N
    error_est = (right - left)**2 * np.sqrt(inside_count * (1 - inside_count/N)) / N

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e}")
