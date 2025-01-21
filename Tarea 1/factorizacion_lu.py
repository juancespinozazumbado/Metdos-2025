import numpy as np

intro = """
    Realiza la factorización LU de una matriz cuadrada no singular A.
    :param A: Matriz cuadrada de tamaño n x n (no singular).
    :return: Matrices L y U tales que A = LU.
    """
    
def lu_factorizacion(A):
    

    n = len(A)
    A = [[float(A[i][j]) for j in range(n)] for i in range(n)]


    #Inicializa matrices L y U
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

        
    for i in range(n):
        # Llenar la fila de U
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        # Llenar la columna de L
        L[i][i] = 1.0  # Diagonal de 1s en L
        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]  # División con floats para precisión    

    return L, U

  
### Imprimir matriz
def print_matriz(M):
    for fila in M:
      print(fila)
    

# Caso de ejemplo
# A =  [[4, 3, 0],
#      [3, 7, -1],
#      [0, -1, 4]]

A = [[2, -1, 1],
     [1, 3, 2],
     [1, -4, -1.5]]

L, U = lu_factorizacion(A)

print(intro)

print("Matriz trinagular: ")
print_matriz(A)

print("\nMatriz L (Triangular inferior):")
print_matriz(L)

print("\nMatriz U (Triangulo superior):")
print_matriz(U)
