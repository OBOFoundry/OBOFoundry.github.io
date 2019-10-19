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
                sh 'kill $(lsof -t -i:25333) || true'
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