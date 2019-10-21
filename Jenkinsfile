pipeline {
    agent any

    stages {
        stage('dashboard') {
            steps {
                sh 'export PYTHONUNBUFFERED=1'
                sh 'make clean-dashboard'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
        }
    }
}