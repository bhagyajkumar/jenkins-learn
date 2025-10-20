pipeline {
    agent any

    post {
        always {
            // Publish styled Pytest report after every run
            publishHTML(target: [
                reportName: 'Pytest Report',
                reportDir: 'report',
                reportFiles: 'index.html',
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

        stage('Setup Virtual Environment') {
            steps {
                echo 'Setting up virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-html-reporter
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest-html-reporter...'
                sh '''
                    . venv/bin/activate
                    pytest --html-report=report --title="Pytest Report" --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Archive Report') {
            steps {
                echo 'Archiving report...'
                archiveArtifacts artifacts: 'report/**', fingerprint: true
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up virtual environment...'
                sh 'rm -rf venv/'
            }
        }
    }
}
