"""Punto de entrada del gestor de tareas."""
from gestor import almacenamiento, estadisticas, tareas

RUTA = "tareas.json"


def main():
    lista = almacenamiento.cargar(RUTA)
    tareas.crear_tarea(lista, "Tarea de ejemplo", "alta")
    print(estadisticas.resumen(lista))
    almacenamiento.guardar(lista, RUTA)


if __name__ == "__main__":
    main()
