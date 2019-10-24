pipeline {
    stages {
        stage('Init') {
            steps {
                parallel(
                    "Report": {
                        sh 'env > env.txt'
                        sh 'echo $BRANCH_NAME > branch.txt'
                        sh 'cat env.txt'
                        sh 'cat branch.txt'
                    })
            }
        }
        stage('Produce dashboard') {
            agent {
                docker {
                    image 'obolibrary/odkfull:v1.1.7'
                    // Reset Jenkins Docker agent default to original
                    // root.
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