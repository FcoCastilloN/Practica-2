def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encuentra el elemento m�nimo en la parte no ordenada
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambia el elemento m�nimo con el elemento en la posici�n actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)

print("Lista ordenada:")
for i in range(len(arr)):
    print(arr[i])
