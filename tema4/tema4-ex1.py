import numpy as np

a, b = 0., .8
func = lambda x : 400*x**5 - 900*x**4 + 675*x**3 - 200*x**2 + 25*x + .2

aprox_trapecio = (b-a)*(func(a) + func(b))/2

c = (a+b)/2
aprox_simpson = (b-a)*(func(a) + 4*func(c) + func(b))/6

print(f"Integral entre a = {a:.1f} e b = {b:.1f}.")
print(f"Aproximación coa regra do trapecio: {aprox_trapecio:.5f}")
print(f"Aproximación coa regra de Simpson 1/3: {aprox_simpson:.5f}")
