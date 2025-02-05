class MergeSort:
    name = "MergeSort"
    complexity = "O(n log n)"
    description = "Algoritmo de ordenamiento basado en la técnica de divide y vencerás."

    @staticmethod
    def sort(arr, draw_array):
        sorted_arr = MergeSort._mergesort(arr, draw_array)
        arr[:] = sorted_arr

    @staticmethod
    def _mergesort(arr, draw_array):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = MergeSort._mergesort(arr[:mid], draw_array)
        right = MergeSort._mergesort(arr[mid:], draw_array)
        return MergeSort._merge(left, right, draw_array)

    @staticmethod
    def _merge(left, right, draw_array):
        sorted_arr = []
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
        sorted_arr.extend(left or right)
        draw_array(sorted_arr)
        return sorted_arr
