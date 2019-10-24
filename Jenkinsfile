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
    docker.image("obolibrary/odkfull:v1.1.7").inside {
        sh 'ls -al'
    }
}