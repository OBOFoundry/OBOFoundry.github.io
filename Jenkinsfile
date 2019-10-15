pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh './build.sh'
                sh 'make build/robot.jar'
            }
        }
        stage('dashboard') {
            steps {
                sh 'kill $(lsof -t -i:25333)'
                sh 'make dashboard'
                sh 'kill $(lsof -t -i:25333)'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*', fingerprint: true
        }
    }
}