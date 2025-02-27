import numpy as np

a, b = 0., 1.35
func = lambda x : x**3 - 3*x**2 - x + 3
stop_threshold = 1e-8

def trapecio_composta(n, f = func, l = a, r = b):

    """
    n : número de subintervalos
    f : función a integrar
    l, r : extremos do intervalo
    """

    h = (r-l)/n
    aprox = (f(l) + f(r))*h/2
    aprox += h*np.sum(np.fromiter((f(l + k*h) for k in range(1,n)), dtype = float))

    return aprox

# Paso inicial
N = 2
prev_aprox = trapecio_composta(N-1)
aprox = trapecio_composta(N)

while not np.abs(aprox - prev_aprox) < stop_threshold:
    N += 1
    prev_aprox = aprox
    aprox = trapecio_composta(N)

print(f"Regra do trapecio composta con {N} subintervalos.")
print(f"A integral entre a = {a:.2f} e b = {b:.2f} resulta: {aprox:.9f}")
