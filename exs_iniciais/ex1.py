import numpy as np

coeffs = np.zeros(3)
for c, coeff in enumerate(coeffs):
    coeffs[c] = input(f"Introduza o coeficiente de orde {c}: ")

disc = coeffs[1]**2 - 4*coeffs[0]*coeffs[2]

if disc < 0:
    print("Discriminante negativo.")
else:
    print(f"x_+ = {(np.sqrt(disc)-coeffs[1])/(2*coeffs[2])}")
    print(f"x_- = {-(np.sqrt(disc)+coeffs[1])/(2*coeffs[2])}")
