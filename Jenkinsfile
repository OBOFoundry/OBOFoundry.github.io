pipeline {
    agent {
        image 'obolibrary/odkfull:v1.1.7'
        args '-u root:root'
    }
    stages {
        stage("Test") {
            steps { 
                sh 'ls -al'
            }
        }
    }
}
