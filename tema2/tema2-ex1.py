import numpy as np

maclaurin = lambda x, n : 1 + np.sum(np.fromiter((x**k/np.prod(range(1,k+1)) for k in range(1,n+1)), float))

a = 0.5

for N in (3,4,5):
    print(f"A serie de MacLaurin da exponencial con {N} termos dá exp({a}) = {maclaurin(a, N)}.")
