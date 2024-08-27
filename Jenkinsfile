pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 hello.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_hello.py'
            }
        }
        stage('Generate Docker Image') {
            steps {
                sh 'docker build -t hello-world .'
            }
        }
        stage('Run Docker Image') {
            steps {
                sh 'docker run hello-world'
            }
        }

    }
}
