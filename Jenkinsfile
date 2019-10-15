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