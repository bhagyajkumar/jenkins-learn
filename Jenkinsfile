pipeline {
    agent any

    post {
        always {
            publishHTML(target: [
                reportName: 'Pytest Report',
                reportDir: '.',
                reportFiles: 'report.html',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: false
            ])
        }
    }


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
                sh 'python3 -m venv venv && . venv/bin/activate && echo "Virtual env activated"'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running test stage...'
                sh './venv/bin/python -m pytest --html=report.html --self-contained-html'

            }
        }

        stage('Archive Report') {
            steps {
                echo 'Archiving test report...'
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }


        stage('Cleanup') {
            steps {
                echo 'Running test Cleanup...'
                sh 'rm -rf venv/'
                sh 'rm report.html'
            }
        }
    }
}
