import numpy as np
import random as rd
import time

bounds = {
    "x" : (1., 4.),
    "y" : (-3., 4.),
    "z" : (-1., 1.)
}
bounding_size = np.prod(np.fromiter((bounds[l][1] - bounds[l][0] for l in ("x","y","z")), dtype = float))
Ns = 10 ** np.array(range(2,9))
r, R = 1., 3.
condition = lambda x, y, z : (np.sqrt(x**2 + y**2) - R)**2 + z**2 < r

print(" "*8 + "N" + " "*8 + "I" + " "*12 + "Erro" + " "*4 + "Tempo")

for N in Ns:

    origin = time.time()

    points_x = np.fromiter((rd.uniform(bounds["x"][0],bounds["x"][1]) for k in range(N)), dtype = float)
    points_y = np.fromiter((rd.uniform(bounds["y"][0],bounds["y"][1]) for k in range(N)), dtype = float)
    points_z = np.fromiter((rd.uniform(bounds["z"][0],bounds["z"][1]) for k in range(N)), dtype = float)
    inside_count = np.sum(condition(points_x, points_y, points_z))

    integral = bounding_size * inside_count / N
    error_est = bounding_size * np.sqrt(inside_count * (1 - inside_count/N)) / N

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e} {time.time() - origin:8.3f}")
