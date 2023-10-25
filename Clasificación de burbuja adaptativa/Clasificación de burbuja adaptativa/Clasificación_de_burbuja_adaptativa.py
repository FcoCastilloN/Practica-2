
def adaptive_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True

        # Si no hubo intercambios en esta pasada, la lista ya est� ordenada
        if not swapped:
            break

        n -= 1  # Reduce el tama�o de la lista para la siguiente pasada

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
adaptive_bubble_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)