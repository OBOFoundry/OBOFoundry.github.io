pipeline {
    agent any
    node {
        stage('Docker') {
            def img = docker.build("obolibrary/odkfull:v1.1.7")
            img.inside {
                sh 'ls -al'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
        }
    }
}