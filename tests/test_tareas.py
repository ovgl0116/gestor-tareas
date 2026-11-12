import unittest

from gestor import tareas


class TestTareas(unittest.TestCase):
    def test_crear_tarea_asigna_id_y_estado(self):
        lista = []
        t = tareas.crear_tarea(lista, "Estudiar Jenkins", "alta")
        self.assertEqual(t["id"], 1)
        self.assertFalse(t["completada"])
        self.assertEqual(len(lista), 1)

    def test_crear_tarea_titulo_vacio(self):
        with self.assertRaises(ValueError):
            tareas.crear_tarea([], "   ")

    def test_crear_tarea_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            tareas.crear_tarea([], "Algo", "urgente")

    def test_completar_tarea(self):
        lista = []
        tareas.crear_tarea(lista, "Hacer pipeline")
        self.assertTrue(tareas.completar_tarea(lista, 1)["completada"])

    def test_completar_tarea_inexistente(self):
        with self.assertRaises(KeyError):
            tareas.completar_tarea([], 99)

    def test_eliminar_tarea(self):
        lista = []
        tareas.crear_tarea(lista, "Borrar")
        self.assertTrue(tareas.eliminar_tarea(lista, 1))
        self.assertEqual(lista, [])


if __name__ == "__main__":
    unittest.main()
