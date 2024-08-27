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
    }
}
