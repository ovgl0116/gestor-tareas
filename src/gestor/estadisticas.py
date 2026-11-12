"""Módulo de estadísticas: resumen del avance de las tareas."""


def resumen(lista):
    """Devuelve total, completadas, pendientes y porcentaje de avance."""
    total = len(lista)
    completadas = sum(1 for t in lista if t["completada"])
    avance = round(completadas * 100 / total, 1) if total else 0.0
    return {
        "total": total,
        "completadas": completadas,
        "pendientes": total - completadas,
        "avance": avance,
    }


def pendientes_por_prioridad(lista):
    """Cuenta las tareas pendientes agrupadas por prioridad."""
    conteo = {"alta": 0, "media": 0, "baja": 0}
    for t in lista:
        if not t["completada"]:
            conteo[t["prioridad"]] += 1
    return conteo
