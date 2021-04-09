Jenkinsfile (Declarative Pipeline)

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python passwordtester.py'
            }
        }
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m pytest testing.py'
            }
        }
    }
}

