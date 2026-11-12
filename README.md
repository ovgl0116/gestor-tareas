# Gestor de tareas (Proyecto parte 1 - Integración Continua)

Aplicación en Python con tres funcionalidades: registrar tareas, completar/eliminar tareas y estadísticas de avance.

## Ejecutar las pruebas
    PYTHONPATH=src python3 -m unittest discover -s tests -t . -v

## Jenkins
- `Dockerfile.jenkins`: imagen de Jenkins con Python (`docker build -t jenkins-python -f Dockerfile.jenkins .`).
- `Jenkinsfile`: pipeline (Checkout, Preparar entorno, Análisis estático, Pruebas).
