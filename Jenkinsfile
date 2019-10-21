pipeline {
    agent any

    stages {
        stage('dashboard') {
            steps {
                sh 'export PYTHONUNBUFFERED=1'
                sh 'make clean-dashboard'
                sh 'kill $(lsof -t -i:25333) || true'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
        }
    }
}