
def lu_factorizacion(A):
    
    n = len(A)

    # Inicializa matrices L y U
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    
    ## implementar logica en caso de que la matriz sea singular
    ## devolver ambas matrices

  
### Imprimir matriz
def print_matriz(M):
    for fila in M:
      print(fila)
    

# Caso de ejemplo
A =  [[4, 3, 0],
     [3, 7, -1],
     [0, -1, 4]]

L, U = lu_factorizacion(A)


print("Matriz trinagular: ")
print_matriz(A)

print("\nMatriz L (Triangular inferior):")
print_matriz(L)

print("\nMatriz U (Triangulo superior):")
print_matriz(U)
