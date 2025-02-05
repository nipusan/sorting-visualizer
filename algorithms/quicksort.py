class QuickSort:
    name = "QuickSort"
    complexity = "O(n log n) promedio, O(n^2) peor caso"
    description = "Algoritmo de ordenamiento rápido basado en el paradigma divide y vencerás."

    @staticmethod
    def sort(arr, draw_array):
        QuickSort._quicksort(arr, draw_array, 0, len(arr) - 1)

    @staticmethod
    def _quicksort(arr, draw_array, low, high):
        if low < high:
            pi = QuickSort._partition(arr, draw_array, low, high)
            QuickSort._quicksort(arr, draw_array, low, pi - 1)
            QuickSort._quicksort(arr, draw_array, pi + 1, high)

    @staticmethod
    def _partition(arr, draw_array, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                draw_array(arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        draw_array(arr)
        return i + 1
