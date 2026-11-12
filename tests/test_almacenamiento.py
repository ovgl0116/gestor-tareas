import os
import tempfile
import unittest

from gestor import almacenamiento, tareas


class TestAlmacenamiento(unittest.TestCase):
    def test_guardar_y_cargar(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = os.path.join(d, "t.json")
            lista = []
            tareas.crear_tarea(lista, "Persistir")
            almacenamiento.guardar(lista, ruta)
            self.assertEqual(almacenamiento.cargar(ruta), lista)

    def test_cargar_archivo_inexistente(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(almacenamiento.cargar(os.path.join(d, "no.json")), [])


if __name__ == "__main__":
    unittest.main()
