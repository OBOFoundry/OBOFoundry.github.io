pipeline {
    agent any
    stages {
        stage('Produce dashboard') {
            agent {
                docker {
                    image 'obolibrary/odkfull:v1.1.7'
                    args '-u root:root'
                }
            }
            steps {
                dir('./OBOFoundry.github.io') {
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