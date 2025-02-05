# 🔥 Sorting Algorithms Visualizer - Pygame

### 📝 **Descripción**
Este proyecto es un **visualizador interactivo de algoritmos de ordenamiento** construido en **Python** con **Pygame**.  
Permite visualizar en **tiempo real** el funcionamiento de distintos algoritmos de ordenamiento mediante **barras animadas**.  

El sistema es **modular**, lo que significa que **se pueden agregar nuevos algoritmos fácilmente** en la carpeta `algorithms/` sin modificar el código principal.

---

## 🚀 **Características**
✅ **Carga dinámica de algoritmos** (cualquier `.py` en `algorithms/` se detecta automáticamente).  
✅ **Menú interactivo con navegación** (`↑`, `↓` para moverse, `Enter` para seleccionar).  
✅ **Visualización en tiempo real con estadísticas** (nombre del algoritmo, iteraciones, tiempo).  
✅ **Modularidad** (agrega algoritmos sin tocar `sorting_visualizer.py`).  
✅ **Optimizado con Pygame** para animaciones fluidas.  

---

## 📂 **Estructura del Proyecto**

```bash
sorting-visualizer/
│── algorithms/             # 📌 Carpeta donde se almacenan los algoritmos de ordenamiento
│   │── bubblesort.py       # Bubble Sort
│   │── insertionsort.py    # Insertion Sort
│   │── selectionsort.py    # Selection Sort
│   │── shellsort.py        # Shell Sort
│   │── quicksort.py        # Quick Sort
│   │── mergesort.py        # Merge Sort
│   │── heapsort.py         # Heap Sort
│   │── timsort.py          # TimSort
│── sorting_visualizer.py   # 🎮 Código principal con la interfaz y ejecución de algoritmos
│── README.md               # 📖 Documentación del proyecto
│── requirements.txt        # 📦 Dependencias del proyecto

```



---

## 🛠 **Requisitos**
Para ejecutar este proyecto necesitas:

🔹 **Python** (3.8 o superior)  
🔹 **Pygame** (para la visualización)  

Si no tienes **Python**, descárgalo en: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 📦 **Instalación y Ejecución**
### 1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/nipusan/sorting-visualizer.git
cd sorting-visualizer
```

## 2️⃣ Crear un entorno virtual (opcional, recomendado)


```bash
python -m venv env
```

- En Windows: 
```bash
env\Scripts\activate
```
- En macOS/Linux:
```bash
source env/bin/activate
```

## 3️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 4️⃣ Ejecutar el programa

```bash
python sorting_visualizer.py
```

## 🎮 Controles del Menú

- ⬆ (Flecha arriba): Moverse hacia arriba.
- ⬇ (Flecha abajo): Moverse hacia abajo.
- Enter: Seleccionar algoritmo y ejecutarlo.
- ESC: Salir del programa.

## 📌 Cómo Agregar un Nuevo Algoritmo

## 1️⃣ Crea un nuevo archivo en algorithms/, por ejemplo:

```bash
algorithms/radixsort.py
```

## 2️⃣ Sigue la estructura de los algoritmos existentes:

```bash

class RadixSort:
    name = "Radix Sort"
    complexity = "O(nk)"
    description = "Ordenamiento basado en dígitos con buckets."

    @staticmethod
    def sort(arr, draw_array):
        # Implementación del algoritmo
        pass
```

## 3️⃣ Ejecuta el programa nuevamente (`python sorting_visualizer.py`).

El nuevo algoritmo aparecerá automáticamente en el menú sin modificar el código principal. 🎉

## 🤝 Contribuciones

¡Sientete libre de contribuir! Puedes:
- [x] Mejorar la interfaz gráfica.
- [x] Agregar más algoritmos.
- [x] Optimizar el rendimiento.
- [x] Reportar bugs o sugerir mejoras.


## 📝 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente, pero se agradecen menciones o estrellas en GitHub ⭐.