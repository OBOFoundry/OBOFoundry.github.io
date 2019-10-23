pipeline {
    agent {
        docker {
            image 'geneontology/dev-base:eb2f253bb0ff780e1b623adde6d5537c55c31224_2019-08-13T163314'
            args "-u root:root --tmpfs /opt:exec -w /opt"
        }
    }

    stages {
        stage('dashboard') {
            steps {
                timeout(time: 8, unit: 'HOURS') {
                    sh 'export PYTHONUNBUFFERED=1'
                    sh 'make clean-dashboard'
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