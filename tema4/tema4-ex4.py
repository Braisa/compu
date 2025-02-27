import numpy as np

func = {
    1.0 : 1.543,
    1.1 : 1.669,
    1.2 : 1.811,
    1.3 : 1.971,
    1.4 : 2.151,
    1.5 : 2.352,
    1.6 : 2.577,
    1.7 : 2.828,
    1.8 : 3.107
}

a, b = 1.0, 1.8
hs = (.1,.2,.4)

def trapecio_composta(f, a, b, h):

    """
    f : función a integrar, representación diccionario
    a, b : extremos do intervalo
    h : tamaño dos intervalos
    """

    n = int((b-a)/h)
    aprox = (f[a] + f[a])*h/2
    aprox += h*np.sum(np.fromiter((f[round(a+k*h, 1)] for k in range(1,n)), dtype = float))

    return aprox

print(f"Integral entre a = {a:.1f} e b = {b:.1f} aproximada coa regra do trapecio composta.")
for h in hs:
    print(f"Con subdivisións de tamaño h = {h:.1f} resulta: {trapecio_composta(func, a, b, h):.4f}")
