# Exercicio resolto dado para corrixir

import numpy as np

# ============ DATOS DE ENTRADA ========================

# Matriz de coeficientes (matriz triangular superior)
a = np.array([[1, 1, -2], [0, -3, 8], [0, 0, -10]], float)

# Vector columna de términos independientes
b = np.array([[9], [-14], [-5]], float)


# ============ MATRIZ AMPLIADA =========================

#Crear matriz ampliada
ab = np.hstack((a, b))
print('Matriz ampliada inicial:')
print(ab, '\n')


# ============ CÁLCULOS: MÉTODO DE GAUSS ===============

print('Método: eliminación de Gauss')

# Determinar número de filas y columnas
numf, numc = np.shape(ab)

# Sustitución regresiva
x = np.zeros((numf, 1))
            
for i in range(2, -1, -1):
    suma = np.dot(ab[i, 0:numf], x)
    x[i] = (ab[i, numc-1] - suma) / ab[i, i]


# ============ IMPRIMIR RESULTADOS =====================

print('='*28)
print('Solución:')

for i in range(numf):
    print(f'x{i+1}= {x[i,0]:.2f}')

print('='*28)