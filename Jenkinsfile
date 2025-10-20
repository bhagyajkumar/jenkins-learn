pipeline {
    agent any

    options {
        skipDefaultCheckout(true) // Prevent Jenkins from doing implicit checkout
    }

    stages {
        stage('Checkout') {
            steps {
                deleteDir() // Clean workspace first
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/bhagyajkumar/jenkins-learn.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Running build stage...'
                sh 'python3 --version' // verify files are cloned
            }
        }

        stage('Test') {
            steps {
                echo 'Running test stage...'
            }
        }
    }
}
