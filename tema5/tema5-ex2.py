import numpy as np
import random as rd
import time

func = lambda x : (1-x**2)**1.5
condition = lambda x, y : y < func(x)
left, right = 0, 1
Ns = 10 ** np.array(range(2,9))

print(" "*8 + "N" + " "*8 + "I" + " "*11 + "Erro" + " "*4 + "Tempo")

for N in Ns:

    origin = time.time()

    # Método Diego
    
    points = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    mean = np.sum(func(points)) / N
    sqmean = np.sum(func(points)**2) / N

    integral = (right - left) * mean
    error_est = (right - left) * np.sqrt((sqmean - mean**2)/N)
    
    # Método Fabián
    """
    points_x = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    points_y = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    inside_count = np.sum(condition(points_x, points_y))

    integral = (right - left)**2 * inside_count / N
    error_est = (right - left)**2 * np.sqrt(inside_count * (1 - inside_count/N)) / N
    """

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e} {time.time() - origin:8.3f}")
