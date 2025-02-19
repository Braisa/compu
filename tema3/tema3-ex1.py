import numpy as np

A = np.array(((1,1,-2),
              (0,-3,8),
              (0,0,-10)))

B = np.atleast_2d(np.array((9,-14,-5))).T

AB = np.hstack((A, B))

print(f"Matriz ampliada:\n{AB}")

sols = np.zeros(3)

# Triangular superior, co cal percorremos en sentido inverso
for i, fila in enumerate(AB[::-1]):
    A_fila, B_i = fila[:-1], fila[-1]
    sols[-i-1] = (B_i - np.dot(A_fila[-1:2-i:-1], sols[-1:2-i:-1]))/A_fila[2-i]

print("Solución por substitución regresiva.")
for i, sol in enumerate(sols):
    print(f"x_{i+1} = {sol:.2f}")
