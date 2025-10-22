pipeline {
    agent any

    post {
        always {
            // Publish HTML report
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])

            // Publish JUnit XML report
            junit 'report.xml'
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

        stage('Setup Environment') {
            steps {
                echo 'Creating and activating virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Pytest...'
                sh '''
                    . venv/bin/activate
                    # Run tests, generate HTML and JUnit XML reports, capture console logs
                    pytest --html=report.html --self-contained-html --junitxml=report.xml -v --capture=tee-sys
                '''
            }
        }

        stage('Convert HTML to PDF') {
            steps {
                echo 'Converting HTML report to PDF...'
                sh '''
                    wkhtmltopdf --enable-local-file-access report.html report.pdf
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving HTML and PDF reports...'
                archiveArtifacts artifacts: 'report.html, report.pdf', fingerprint: true
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                sh 'rm -rf venv/ report.html report.pdf report.xml'
            }
        }
    }
}
