import numpy as np

mat = np.array(((1, 1, 1, 1, 1, 10),
                (2, 2, 2, 2, 2, 20),
                (3, 3, 3, 3, 3, 30),
                (4, 5, 6, 7, 8, 90)))

print(mat)
print("Intercámbianse os elementos das posicións (1,6) e (4,6).")

mat[0,5], mat[3,5] = mat[3,5], mat[0,5]
print(mat)
