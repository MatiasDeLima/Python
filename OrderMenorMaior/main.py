

def HeapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n -1 , 0 , -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

array = list(map(int, input(
    "Enter the elemets: ").split()))
HeapSort(array)
print("Sorted array: ", array);