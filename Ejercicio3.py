import numpy as np

def ordenarFilas_Matriz(arr, n):
    # Caso base: si la longitud del arreglo es 1, ya está ordenado
    if n == 1:
        return arr
    else:
        ordenarFilas_Matriz(arr, n - 1)
        ultimo = arr[n-1]
        j = n-2
        while j >= 0 and arr[j] > ultimo:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = ultimo
    return np.array(arr)


m = [[12, 2, 23, 9, 20, 5], [1, 12, 3, 19, 20, 15],
     [12, 2, 2, 3, 20, 9], [12, 2, 7, 6, 10, 13],
     [1, 15, 20, 19, 2, 5], [12, 8, 23, 5, 8, 25]]
for fila in m:
    print(ordenarFilas_Matriz(fila, len(fila)))










#print(x[i])