pipeline {
    agent any

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

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --html=report.html --self-contained-html --junitxml=report.xml -v --capture=tee-sys --alluredir=allure-results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --alluredir=allure-results -v
                '''
            }
        }



        stage('Convert HTML to PDF') {
            steps {
                sh 'wkhtmltopdf --enable-local-file-access report.html report.pdf'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'report.html, report.pdf', fingerprint: true
            }
        }
    }

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

            // Now cleanup AFTER publishing
            sh 'rm -rf venv/ report.html report.pdf report.xml'
        }
    }
}
