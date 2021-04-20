pipeline {
    agent {
        docker { image 'python:3.8-slim-buster' }
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python passwordtester.py'
            }
        }
        stage('test') {
            steps {
                sh 'python -m pytest testing.py'
            }
        }
    }
}

