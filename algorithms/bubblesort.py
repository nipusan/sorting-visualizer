class BubbleSort:
    name = "Bubble Sort"
    complexity = "O(n^2)"
    description = "Algoritmo simple que compara y cambia elementos adyacentes repetidamente."

    @staticmethod
    def sort(arr, draw_array):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    draw_array(arr)
                    swapped = True
            if not swapped:  # Optimización: Si no hubo intercambios, ya está ordenado.
                break
