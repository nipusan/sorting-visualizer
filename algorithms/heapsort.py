class HeapSort:
    name = "HeapSort"
    complexity = "O(n log n)"
    description = "Algoritmo de ordenamiento basado en la estructura de montículos."

    @staticmethod
    def sort(arr, draw_array):
        HeapSort._heapsort(arr, draw_array)

    @staticmethod
    def _heapsort(arr, draw_array):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify(arr, draw_array, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            draw_array(arr)
            HeapSort._heapify(arr, draw_array, i, 0)

    @staticmethod
    def _heapify(arr, draw_array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            draw_array(arr)
            HeapSort._heapify(arr, draw_array, n, largest)
