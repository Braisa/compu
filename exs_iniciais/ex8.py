import numpy as np

mat = np.array(((1, 1, 1, 1, 1, 10),
                (2, 2, 2, 2, 2, 20),
                (3, 3, 3, 3, 3, 30),
                (4, 5, 6, 7, 8, 90)))

print(mat)
print("Intercámbianse as filas 2 e 4.")

matp = np.copy(mat)
matp[1], matp[3] = mat[3], mat[1]
print(matp)
