"""Módulo de tareas: crear, completar y eliminar."""


def crear_tarea(lista, titulo, prioridad="media"):
    """Agrega una tarea nueva a la lista y la devuelve."""
    if not titulo or not titulo.strip():
        raise ValueError("El título no puede estar vacío")
    if prioridad not in ("alta", "media", "baja"):
        raise ValueError("Prioridad inválida")
    tarea = {
        "id": max((t["id"] for t in lista), default=0) + 1,
        "titulo": titulo.strip(),
        "prioridad": prioridad,
        "completada": False,
    }
    lista.append(tarea)
    return tarea


def completar_tarea(lista, id_tarea):
    """Marca una tarea como completada."""
    for tarea in lista:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            return tarea
    raise KeyError(f"No existe la tarea {id_tarea}")


def eliminar_tarea(lista, id_tarea):
    """Elimina una tarea de la lista."""
    for tarea in lista:
        if tarea["id"] == id_tarea:
            lista.remove(tarea)
            return True
    raise KeyError(f"No existe la tarea {id_tarea}")
