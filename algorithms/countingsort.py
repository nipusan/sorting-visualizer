class CountingSort:
    name = "Counting Sort"
    complexity = "O(n + k)"
    description = "Algoritmo eficiente para ordenar números en un rango conocido, basado en conteo de ocurrencias."

    @staticmethod
    def sort(arr, draw_array):
        if not arr:
            return
        max_val = max(arr)
        min_val = min(arr)
        range_size = max_val - min_val + 1

        count = [0] * range_size
        output = [0] * len(arr)

        for num in arr:
            count[num - min_val] += 1
        draw_array(count)

        for i in range(1, len(count)):
            count[i] += count[i - 1]
        draw_array(count)

        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
            draw_array(output)

        arr[:] = output
        draw_array(arr)
