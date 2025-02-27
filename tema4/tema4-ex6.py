import numpy as np

a, b = 0., 1.
func = lambda x, n : x**n * np.exp(x)
N = 5

def trapecio_composta(f, n, l = a, r = b, N = N):

    """
    f : función a integrar
    n : orde de recorrencia
    l, r : extremos do intervalo
    N : número de subintervalos
    """

    h = (r-l)/N
    aprox = (f(l, n) + f(r, n))*h/2
    aprox += h*np.sum(np.fromiter((f(l + k*h, n) for k in range(1,N)), dtype = float))

    return aprox

print(f"Integral entre a = {a:.1f} e b = {b:.1f}.")
print(43*" " + f"Recorrencia | Trapecio composta con {N} subintervalos")

# Paso inicial
I_n = np.e - 1
print(f"Para a orde de recorencia n = {0}, resulta : {I_n:12.5f}" + f"| {trapecio_composta(func, 0):.5f}")

for n in range(1,8):
    I_n = np.e - n*I_n
    print(f"Para a orde de recorencia n = {n}, resulta : {I_n:12.5f}" + f"| {trapecio_composta(func, n):.5f}")
