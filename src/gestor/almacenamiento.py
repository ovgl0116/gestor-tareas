"""Módulo de almacenamiento: guarda y carga tareas en un archivo JSON."""
import json
import os


def guardar(lista, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def cargar(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)
