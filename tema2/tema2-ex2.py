import numpy as np

h = .25
func = lambda x : -.1*x**4 -.15*x**3 -.5*x**2 - .25*x + 1.2
c = .5

print("As aproximacións por diferencias finitas para a derivada numérica son as seguintes:")
print(f"Cara adiante f'(0.5) = {(func(c+h)-func(c))/h:.4f}.")
print(f"Cara atrás f'(0.5) = {(func(c)-func(c-h))/h:.4f}.")
print(f"Centradas f'(0.5) = {(func(c+h)-func(c-h))/2/h:.4f}.")
