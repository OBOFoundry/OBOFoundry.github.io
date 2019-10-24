node {
    stage "Test Docker"
    def img = docker.build("obolibrary/odkfull:v1.1.7")
    img.inside {
        sh 'ls -al'
        sh 'robot help'
    }
}