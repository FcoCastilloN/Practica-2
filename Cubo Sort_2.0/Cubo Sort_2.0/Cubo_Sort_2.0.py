def bucket_sort(arr):
    return sorted_buckets

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bucket_sort(arr)

print("Lista ordenada:")
for element in sorted_arr:
    print(element)
