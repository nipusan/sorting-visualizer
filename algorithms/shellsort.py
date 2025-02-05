class ShellSort:
    name = "Shell Sort"
    complexity = "O(n log n) a O(n^2)"
    description = "Extensión del Insertion Sort que usa incrementos decrecientes para mejorar el rendimiento."

    @staticmethod
    def sort(arr, draw_array):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                    draw_array(arr)
                arr[j] = temp
                draw_array(arr)
            gap //= 2
