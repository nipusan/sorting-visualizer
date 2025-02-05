class SelectionSort:
    name = "Selection Sort"
    complexity = "O(n^2)"
    description = "Selecciona repetidamente el elemento más pequeño y lo intercambia con la primera posición no ordenada."

    @staticmethod
    def sort(arr, draw_array):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw_array(arr)
