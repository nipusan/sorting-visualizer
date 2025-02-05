import pygame
import random
import time

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE, ORANGE, PURPLE, CYAN = (
    (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 165, 0), (128, 0, 128), (0, 255, 255)
)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualización de Algoritmos de Ordenamiento")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Variables de estadísticas
iterations = 0
start_time = 0
algo_name = ""

# Función para dibujar estadísticas en pantalla
def draw_stats():
    screen.fill(BLACK, (0, 0, WIDTH, 40))  # Limpiar el área de estadísticas
    elapsed_time = round(time.time() - start_time, 4)
    stats_text = f"Algoritmo: {algo_name} | Iteraciones: {iterations} | Tiempo: {elapsed_time} s | Elementos: {array_size}"
    text = font.render(stats_text, True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.update()

# Función para dibujar las barras
def draw_array(arr, colors):
    global iterations
    iterations += 1
    draw_stats()
    
    screen.fill(BLACK, (0, 40, WIDTH, HEIGHT - 40))  # Limpiar solo el área de barras
    bar_width = WIDTH // len(arr)
    max_height = max(arr)
    
    for i, val in enumerate(arr):
        x = i * bar_width
        y = HEIGHT - (val / max_height) * (HEIGHT - 50)
        pygame.draw.rect(screen, colors[i], (x, y, bar_width - 2, HEIGHT - y))

    pygame.display.update()
    time.sleep(0.02)  # Pequeña pausa para hacer la animación más fluida

# Función genérica de animación
def visualize_sort(sort_function, arr, title):
    global iterations, start_time, algo_name
    iterations = 0
    start_time = time.time()
    algo_name = title

    pygame.display.set_caption(title)
    colors = [WHITE] * len(arr)
    sort_function(arr, colors)
    draw_array(arr, colors)
    time.sleep(1)  # Pausa final para ver el resultado ordenado

# QUICK SORT
def quicksort(arr, colors, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                colors[i], colors[j] = RED, RED
                draw_array(arr, colors)
                colors[i], colors[j] = WHITE, WHITE
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        draw_array(arr, colors)
        return i + 1

    if low < high:
        pi = partition(low, high)
        quicksort(arr, colors, low, pi - 1)
        quicksort(arr, colors, pi + 1, high)

# MERGE SORT
def mergesort(arr, colors):
    def merge(left, right):
        sorted_arr = []
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
        sorted_arr.extend(left or right)
        return sorted_arr

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        sorted_arr = merge(left, right)
        draw_array(sorted_arr, [BLUE] * len(sorted_arr))
        return sorted_arr

    arr[:] = sort(arr)

# HEAP SORT
def heapsort(arr, colors):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            colors[i], colors[largest] = PURPLE, PURPLE
            draw_array(arr, colors)
            colors[i], colors[largest] = WHITE, WHITE
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        colors[i], colors[0] = ORANGE, ORANGE
        draw_array(arr, colors)
        colors[i], colors[0] = WHITE, WHITE
        heapify(i, 0)

# TIMSORT (Python interno)
def timsort(arr, colors):
    arr.sort()
    draw_array(arr, [CYAN] * len(arr))

# Función principal con menú interactivo
def main():
    global array_size
    running = True
    while running:
        # Dibujar el menú
        screen.fill(BLACK)
        text_lines = [
            "Seleccione un algoritmo de ordenamiento:",
            "1 - QuickSort",
            "2 - MergeSort",
            "3 - HeapSort",
            "4 - Timsort",
            "ESC - Salir"
        ]

        for i, line in enumerate(text_lines):
            text = font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 4, HEIGHT // 3 + i * 40))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                array_size = 50
                arr = [random.randint(10, 500) for _ in range(array_size)]
                
                if event.key == pygame.K_1:
                    visualize_sort(quicksort, arr.copy(), "QuickSort")
                elif event.key == pygame.K_2:
                    visualize_sort(mergesort, arr.copy(), "MergeSort")
                elif event.key == pygame.K_3:
                    visualize_sort(heapsort, arr.copy(), "HeapSort")
                elif event.key == pygame.K_4:
                    visualize_sort(timsort, arr.copy(), "Timsort (Python Sort)")
                elif event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
