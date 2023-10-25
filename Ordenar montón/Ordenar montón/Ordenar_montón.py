def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un mont�n m�ximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Intercambiar el m�ximo con el �ltimo elemento
        heapify(arr, i, 0)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)
