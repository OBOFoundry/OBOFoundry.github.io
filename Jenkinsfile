pipeline {
    agent any
    environment {
        TARGET_ADMIN_EMAILS = 'james@overton.ca'
    }

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

        failure {
        echo "There has been a failure in the ${env.BRANCH_NAME} pipeline."
        mail bcc: '', body: "There has been a pipeline failure in ${env.BRANCH_NAME}. Please see: https://build.obolibrary.io/job/obofoundry/job/OBOFoundry.github.io/${env.BRANCH_NAME}", cc: '', from: '', replyTo: '', subject: "OBO Foundry Pipeline FAIL for ${env.BRANCH_NAME}", to: "${TARGET_ADMIN_EMAILS}"
        }
    }
}