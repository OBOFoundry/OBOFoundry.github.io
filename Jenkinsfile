#!groovy

pipeline {
    agent any
    stages {
        stage("Test") {
            steps { test() }
        }
    }
}

def test() {
    withDockerContainer("obolibrary/odkfull:v1.1.7") {
        sh 'ls -al'
    }
}