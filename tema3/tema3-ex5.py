import numpy as np

beta = 1e-20

A1 = np.array(((beta, 1),
               (1,1)))
A2 = A1[::-1]

B1 = np.array((1,2)).reshape((2,1))
B2 = B1[::-1]

AB1, AB2 = np.hstack((A1,B1)), np.hstack((A2,B2))

for n, (case, AB, B) in enumerate(zip(("A","B"),(AB1,AB2),(B1,B2))):

    print(f"\nCaso {case}")
    print(f"Matriz ampliada inicial\n{AB}")

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
        print(f"x_{s+1} = {sol[0]:.2f}")
