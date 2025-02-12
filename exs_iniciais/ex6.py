import numpy as np

mat = np.array(((1, 1, 1, 1, 1, 10),
                (2, 2, 2, 2, 2, 20),
                (3, 3, 3, 3, 3, 30),
                (4, 5, 6, 7, 8, 90)))

print(f"A suma dos elementos da última fila resulta {np.sum(mat[-1])}")
