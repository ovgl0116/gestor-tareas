pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    triggers {
        // Respaldo si no se usa webhook: revisa cambios cada ~2 min
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Analisis estatico') {
            steps {
                sh '''
                    . .venv/bin/activate
                    flake8 --max-line-length=100 src tests
                '''
            }
        }

        stage('Pruebas automaticas') {
            steps {
                sh '''
                    . .venv/bin/activate
                    PYTHONPATH=src python -m xmlrunner discover \
                        -s tests -t . -o reports
                '''
            }
        }
    }

    post {
        always  { junit allowEmptyResults: true, testResults: 'reports/*.xml' }
        success { echo 'Integracion correcta: el codigo paso todas las etapas.' }
        failure { echo 'Integracion fallida: revisar la etapa marcada en rojo.' }
    }
}
