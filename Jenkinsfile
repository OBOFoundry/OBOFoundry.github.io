pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'export PATH=${PATH}:/usr/local/bin'
                sh 'pip install -r requirements.txt'
                sh 'make build/robot.jar'
            }
        }
        stage('dashboard') {
            steps {
                sh 'make dashboard'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*', fingerprint: true
        }
    }
}