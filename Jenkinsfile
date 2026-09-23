pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m venv .venv'
                bat '.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.\\.venv\\Scripts\\python.exe -m compileall app.py'
            }
        }

        stage('Test') {
            steps {
                bat '.\\.venv\\Scripts\\python.exe -m unittest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t jenkins-docker-demo:latest .'
            }
        }

        stage('Docker Run/Deploy') {
            steps {
                bat 'docker rm -f jenkins-demo-app 2>NUL || echo No existing container'
                bat 'docker run -d --name jenkins-demo-app -p 5000:5000 jenkins-docker-demo:latest'
            }
        }
    }
}