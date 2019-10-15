pipeline {
    agent any

    stages {
        stage('Build') {
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