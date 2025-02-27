import numpy as np

a, b = 1, 3
f1 = lambda x : 1/(1+x**2)
f2 = lambda x : np.log(1+x)

n = 5
h = (b-a)/n

print(f"Integral entre a = {a} e b = {b} empregando a regra do trapecio composta con {n} subintervalos.")
for i, f in enumerate((f1,f2)):

    aprox = (f(a) + f(b))*h/2
    aprox += h*np.sum(np.fromiter((f(a + k*h) for k in range(1,n)), dtype = float))

    print(f"A integral I_{i+1} resulta {aprox:.7f}")

# Alternativamente

def trapecio_composta(f, a, b, n):

    """
    f : función a integrar
    a, b : extremos do intervalo
    n : número de subintervalos
    """

    h = (b-a)/n
    aprox = (f(a) + f(b))*h/2
    aprox += h*np.sum(np.fromiter((f(a + k*h) for k in range(1,n)), dtype = float))

    return aprox

print(f"Alternativamente, chamando a unha función que contén o cálculo.")
print(f"A integral I_1 resulta {trapecio_composta(f1,a,b,n):.7f}")
print(f"A integral I_2 resulta {trapecio_composta(f2,a,b,n):.7f}")
