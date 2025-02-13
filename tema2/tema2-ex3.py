import numpy as np

phi = {
    6 : 1.24110,
    7 : 1.40917,
    8 : 1.66863,
    9 : 2.07301,
    10 : 2.71828
}

c = 8
h1 = 1
h2 = 2

for h in (h1,h2):
    print(f"Derivada numérica centrada aproximando por dous puntos con h = {h/10} resulta phi'(0.8) = {(phi[c+h]-phi[c-h])/2/h*10}.")

print(f"Derivada numérica centrada aproximando por catro puntos con h = {h1/10} resulta phi'(0.8) = {((phi[c-h2]-phi[c+h2] + 8*(phi[c+h1]-phi[c-h1]))/12/h1*10)}.")
