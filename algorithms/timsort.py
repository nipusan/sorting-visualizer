class TimSort:
    name = "Timsort"
    complexity = "O(n log n)"
    description = "Algoritmo híbrido de ordenamiento basado en MergeSort e InsertionSort."

    @staticmethod
    def sort(arr, draw_array):
        arr.sort()
        draw_array(arr)
