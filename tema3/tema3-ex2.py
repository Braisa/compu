import numpy as np

A = np.array(((6,-2,2,4),
              (12,-8,6,10),
              (3,-13,9,5),
              (-6,4,1,-2)))
B = np.atleast_2d(np.array((12,18,-30,-9))).T
AB = np.hstack((A,B))

for i in range(np.size(B)):
    
    columna = AB.T[i]

    mults_zeroes = np.zeros(i+1)
    mults_rest = np.ones(np.size(columna)-i-1)
    mults = np.hstack((mults_zeroes, mults_rest))
    
    mults *= columna/columna[i]
    substract = np.tensordot(mults, AB[i], axes = 0)

    AB = AB - substract
