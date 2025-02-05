import pygame
import random
import time
import os
import importlib.util

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, GRAY, YELLOW = (255, 255, 255), (0, 0, 0), (150, 150, 150), (255, 255, 0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualización de Algoritmos de Ordenamiento")
font = pygame.font.Font(None, 36)

# Variables de estadísticas
iterations = 0
start_time = 0
algo_name = ""

# Cargar algoritmos dinámicamente desde el directorio "algorithms"
def load_algorithms():
    algorithms = []
    for file in os.listdir("algorithms"):
        if file.endswith(".py"):
            module_name = file[:-3]  # Quitar la extensión .py
            module_path = os.path.join("algorithms", file)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Buscar una clase dentro del módulo
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and attr.__module__ == module_name:
                    algorithms.append(attr)
                    break  # Tomamos la primera clase encontrada
    return algorithms

algorithms = load_algorithms()

# Función para dibujar estadísticas en pantalla
def draw_stats():
    screen.fill(BLACK, (0, 0, WIDTH, 40))  # Limpiar el área de estadísticas
    elapsed_time = round(time.time() - start_time, 4)
    stats_text = f"Algoritmo: {algo_name} | Iteraciones: {iterations} | Tiempo: {elapsed_time} s | Elementos: {array_size}"
    text = font.render(stats_text, True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.update()

# Función para dibujar las barras
def draw_array(arr):
    global iterations
    iterations += 1
    draw_stats()
    
    screen.fill(BLACK, (0, 40, WIDTH, HEIGHT - 40))  # Limpiar solo el área de barras
    bar_width = WIDTH // len(arr)
    max_height = max(arr)
    
    for i, val in enumerate(arr):
        x = i * bar_width
        y = HEIGHT - (val / max_height) * (HEIGHT - 50)
        pygame.draw.rect(screen, WHITE, (x, y, bar_width - 2, HEIGHT - y))

    pygame.display.update()
    time.sleep(0.02)  # Pequeña pausa para hacer la animación más fluida

# Función para visualizar los algoritmos disponibles en el menú dinámico
def draw_menu(selected_index):
    screen.fill(BLACK)
    title_text = font.render("Seleccione un algoritmo de ordenamiento:", True, WHITE)
    screen.blit(title_text, (WIDTH // 6, HEIGHT // 6))

    for i, algo in enumerate(algorithms):
        text_color = YELLOW if i == selected_index else WHITE  # Resaltar opción seleccionada
        text = font.render(f"{i+1}. {algo.name} ({algo.complexity})", True, text_color)
        screen.blit(text, (WIDTH // 6, HEIGHT // 4 + i * 40))

    exit_text = font.render("ESC - Salir", True, GRAY)
    screen.blit(exit_text, (WIDTH // 6, HEIGHT - 50))

    pygame.display.update()

# Función principal con menú interactivo mejorado
def main():
    global algo_name, start_time, iterations, array_size

    selected_index = 0  # Índice de la opción seleccionada en el menú
    running = True
    while running:
        draw_menu(selected_index)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Salir
                    running = False
                elif event.key == pygame.K_DOWN:  # Mover hacia abajo
                    selected_index = (selected_index + 1) % len(algorithms)
                elif event.key == pygame.K_UP:  # Mover hacia arriba
                    selected_index = (selected_index - 1) % len(algorithms)
                elif event.key == pygame.K_RETURN:  # Seleccionar algoritmo
                    selected_algo = algorithms[selected_index]

                    # Configuración para la ejecución
                    algo_name = selected_algo.name
                    array_size = 50
                    arr = [random.randint(10, 500) for _ in range(array_size)]
                    iterations = 0
                    start_time = time.time()

                    # Ejecutar el algoritmo con animación
                    selected_algo.sort(arr, draw_array)
                    time.sleep(1)  # Pausa al final para ver el resultado ordenado

    pygame.quit()

if __name__ == "__main__":
    main()
