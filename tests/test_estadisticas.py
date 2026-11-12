import unittest

from gestor import estadisticas, tareas


class TestEstadisticas(unittest.TestCase):
    def test_resumen_lista_vacia(self):
        self.assertEqual(estadisticas.resumen([])["avance"], 0.0)

    def test_resumen_con_tareas(self):
        lista = []
        tareas.crear_tarea(lista, "A")
        tareas.crear_tarea(lista, "B")
        tareas.completar_tarea(lista, 1)
        esperado = {"total": 2, "completadas": 1, "pendientes": 1, "avance": 50.0}
        self.assertEqual(estadisticas.resumen(lista), esperado)

    def test_pendientes_por_prioridad(self):
        lista = []
        tareas.crear_tarea(lista, "A", "alta")
        tareas.crear_tarea(lista, "B", "baja")
        tareas.completar_tarea(lista, 2)
        esperado = {"alta": 1, "media": 0, "baja": 0}
        self.assertEqual(estadisticas.pendientes_por_prioridad(lista), esperado)


if __name__ == "__main__":
    unittest.main()
