class InsertionSort:
    name = "Insertion Sort"
    complexity = "O(n^2)"
    description = "Inserta elementos uno por uno en la posición correcta, simulando un ordenamiento manual."

    @staticmethod
    def sort(arr, draw_array):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                draw_array(arr)
            arr[j + 1] = key
            draw_array(arr)
