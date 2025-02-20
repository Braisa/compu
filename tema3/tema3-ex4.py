import numpy as np

A = np.array(((9,-4,0,0),
              (-4,6,0,0),
              (0,0,8,-3),
              (0,0,-3,7)))

B = np.array((20,-10,-20,10)).reshape((4,1))

AB = np.hstack((A,B))#[::-1]
print(f"Matriz ampliada inicial\n{AB}")

# Reordenación das filas para evitar un cero no primeiro pivote
first_nonzero_piv = np.where(AB[:,0] != 0)[0][0]
AB = np.vstack((AB,AB))[first_nonzero_piv:first_nonzero_piv+np.size(B)]

AB_tri = AB

for i in range(np.size(B)-1):

    piv, fila_piv = AB_tri[i,i], AB_tri[i,:]
    col = np.hstack((np.zeros(i+1), AB_tri[i+1:,i]))
    
    AB_tri = AB_tri - np.tensordot(col/piv, fila_piv, axes = 0)

print(f"Matriz triangular resultante\n{AB_tri}")

sols = np.zeros((np.size(B),1))
filas, cols = np.shape(AB_tri)

for i in range(np.size(B)-1, -1, -1):
    sols[i] = (AB_tri[i, cols-1] - np.dot(AB_tri[i,0:filas], sols)) / AB_tri[i,i]

print("Solución por substitución regresiva")
for s, sol in enumerate(sols):
    print(f"I_{s+1} = {sol[0]:.2f} A")