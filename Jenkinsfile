pipeline {
    agent any
    stages {
        stage('dashboard') {
            agent {
                docker {
                    image 'geneontology/dev-base:eb2f253bb0ff780e1b623adde6d5537c55c31224_2019-08-13T163314'
                    args "-u root:root --tmpfs /opt:exec -w /opt"
                }
            }
            steps {
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