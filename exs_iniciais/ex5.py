import numpy as np

mat = np.array(((1, 1, 1, 1, 1, 10),
                (2, 2, 2, 2, 2, 20),
                (3, 3, 3, 3, 3, 30),
                (4, 5, 6, 7, 8, 90)))

print(f"A matriz ten {mat.shape[0]} filas e {mat.shape[1]} columnas.")
print(f"A matriz ten {len(mat[0:,])} filas e {len(mat[0])} columnas.")
# Sen funcións preexistentes?
