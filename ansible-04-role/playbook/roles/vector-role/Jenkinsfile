pipeline {
    agent {
        label 'linux'
    }
    stages {
        stage('test role') {
            steps {
                sh 'molecule test'
            }
        }
    }
}