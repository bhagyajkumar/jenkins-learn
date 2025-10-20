pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/bhagyajkumar/jenkins-learn.git'
            }
        }

        stage('VirtualEnvironment') {
            steps {
                echo 'Running build stage...'
                sh 'python3 -m venv venv && source venv/bin/activate'
            }
        }

        stage('Test') {
            steps {
                echo 'Running test stage...'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Running test stage...'
                sh 'rm -rf venv/'
            }
        }
    }
}
