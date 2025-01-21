import numpy as np

intro = """
    Realiza la factorización LU de una matriz cuadrada no singular A.
    :param A: Matriz cuadrada de tamaño n x n (no singular).
    :return: Matrices L y U tales que A = LU.
    """
    
def lu_factorizacion(A):
    
    
    n = A.shape[0]
    L = np.eye(n)  # Matriz identidad inicial para L
    U = A.copy()   # Copia de A para trabajar en la matriz U

    # # implementar logica en caso de que la matriz sea singular
    # # devolver ambas matrices
    for i in range(n):
        if U[i, i] == 0:
            raise ValueError("La matriz es singular y no puede factorizarse en LU.")
            
    # Descompocision LU
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    return L, U

  
### Imprimir matriz
def print_matriz(M):
    for fila in M:
      print(fila)
    

# Caso de ejemplo
# A =  [[4, 3, 0],
#      [3, 7, -1],
#      [0, -1, 4]]

A = np.array([[2, -1, 1],
     [1, 3, 2],
     [1, -4, -1.5]])

L, U = lu_factorizacion(A)

print(intro)

print("Matriz trinagular: ")
print_matriz(A)

print("\nMatriz L (Triangular inferior):")
print_matriz(L)

print("\nMatriz U (Triangulo superior):")
print_matriz(U)
