import numpy as np

a, b = 0., .8
func = lambda x : 400*x**5 - 900*x**4 + 675*x**3 - 200*x**2 + 25*x + .2

h = (b-a)/3
aprox_simpson_38 = (func(a) + 3*func(a + h) + 3*func(a + 2*h) + func(b))*3*h/8

print(f"Integral entre a = {a:.1f} e b = {b:.1f}.")
print(f"Aproximación coa regra de Simpson 3/8: {aprox_simpson_38:.5f}")
