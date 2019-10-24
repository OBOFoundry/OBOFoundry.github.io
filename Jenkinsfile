pipeline {
    agent any

    environment {
        //
        // Run variables
        //
        REPO = 'OBOFoundry.github.io'
    }

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
                    git branch: 'dashboard', url: 'https://github.com/OBOFoundry/$REPO.git'
                }
                timeout(time: 8, unit: 'HOURS') {
                    sh 'ls'
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