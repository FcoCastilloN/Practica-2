def insertion_sort(arr, left=0, right=None):
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
        arr[left + i] = temp[i]

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = min((start + size - 1), (n - 1))
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, midpoint, end)
        size *= 2

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
timsort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)
