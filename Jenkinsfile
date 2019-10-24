pipeline {
    agent {
        docker {
            image 'obolibrary/odkfull:v1.1.7'
            args '-u root:root'
        }
    }
    stages {
        stage('dashboard') {
            steps {
                sh 'mkdir dashboard'
                sh 'ls -al'
                dir('./dashboard') {
                    git branch: 'dashboard', url: 'https://github.com/OBOFoundry/OBOFoundry.github.io.git'
                    sh 'ls -al'
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
        }
    }
}