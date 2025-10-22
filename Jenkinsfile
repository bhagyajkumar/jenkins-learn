pipeline {
    agent any

    environment {
        PATH = "/opt/allure/bin:${env.PATH}"
    }


    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                git branch: 'main', url: 'https://github.com/bhagyajkumar/jenkins-learn.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Allure Report') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --alluredir=allure-results -v
                '''
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            }
        }
    }
}
