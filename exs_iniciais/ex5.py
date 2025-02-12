import numpy as np

mat = np.array(((1, 1, 1, 1, 1, 10),
                (2, 2, 2, 2, 2, 20),
                (3, 3, 3, 3, 3, 30),
                (4, 5, 6, 7, 8, 90)))

print(f"A matriz ten {mat.shape[0]} filas e {mat.shape[1]} columnas.")
print(f"A matriz ten {len(mat)} filas e {len(mat[0])} columnas.")

filas, elementos = 0, 0
for i, fila in enumerate(mat):
    filas += 1
    for j, elem in enumerate(mat[i]):
        elementos += 1
columnas = elementos / filas
print(f"A matriz ten {filas} filas e {columnas} columnas.")
