import numpy as np
import random as rd

func = lambda y : np.exp(-(1/y - 1))/y**2
left, right = 0, 1
Ns = 10 ** np.array(range(2,9))

print(" "*8 + "N" + " "*8 + "I" + " "*9 + "Erro")

for N in Ns:
    points = np.fromiter((rd.uniform(left, right) for k in range(N)), dtype = float)
    mean = 1/N * np.sum(func(points))
    sqmean = 1/N * np.sum(func(points)**2)

    integral = (right - left) * mean
    error_est = (right - left) * np.sqrt((sqmean - mean**2)/N)

    print(f"{N:9.0f} {integral:.12f} {error_est:.2e}")
