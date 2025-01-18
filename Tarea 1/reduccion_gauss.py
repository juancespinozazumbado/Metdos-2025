

def gaussian_elimination_to_int(A, b):
   
    n = len(A)
    
    # Trabajamos inicialmente con flotantes para cálculos internos
    A = A.astype(float)
    b = b.astype(float)

    # Eliminación Gaussiana
    for i in range(n):
        # Pivoteo parcial para asegurar que A[i, i] no sea cero
        if A[i, i] == 0:
            for k in range(i + 1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]  # Intercambio de filas
                    b[[i, k]] = b[[k, i]]
                    break
            else:
                raise ValueError("La matriz es singular y no tiene solución única.")

        # Escalonar
      

# # Ejemplo de uso
A = [[2, -1, 1], [1, 3, 2], [1, 0, 0]]
b = [2, 6, 1]

print("Matriz: ", A)
print("Vector: ", b)

x = gaussian_elimination_to_int(A, b)

print("Vector solución x :", x)