import numpy as np

A = np.array(((1,2,-1),
              (2,4,5),
              (3,-1,-2)))
B = np.array((2,25,-5)).reshape((3,1))

AB = np.hstack((A,B))

print(f"Matriz ampliada inicial\n{AB}")

def find_piv_row(mat, col):
    row = col
    for test_row in range(col+1, np.shape(mat)[0]):
        if np.abs(mat[test_row,col]/mat[row,col]) > 1:
            row = test_row
    return row

AB_tri = AB

for i in range(np.size(B)-1):

    # Atopar a posición do pivote parcial
    row = find_piv_row(AB_tri, i)
    # Intercambiamos as filas correspondentes
    aux_row = AB_tri[row,:].copy()
    AB_tri[row,:], AB_tri[i,:] = AB_tri[i,:], aux_row

    print(f"\nPaso {i+1}")
    if row != i:
        print(f"Fíxose pivote entre as filas {i+1} e {row+1}\n{AB_tri}")

    piv, fila_piv = AB_tri[i,i], AB_tri[i,:]
    col = np.hstack((np.zeros(i+1), AB_tri[i+1:,i]))
    
    AB_tri = AB_tri - np.tensordot(col/piv, fila_piv, axes = 0)

    print(f"Eliminación de Gauss\n{AB_tri}")

print(f"\nMatriz triangular resultante\n{AB_tri}\n")

sols = np.zeros((np.size(B),1))
filas, cols = np.shape(AB_tri)

for i in range(np.size(B)-1, -1, -1):
    sols[i] = (AB_tri[i, cols-1] - np.dot(AB_tri[i,0:filas], sols)) / AB_tri[i,i]

print("Solución por substitución regresiva")
for s, sol in enumerate(sols):
    print(f"x_{s+1} = {sol[0]:.2f}")
