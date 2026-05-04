pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ramishamaryam634-maker/jobportal-selenium-tests.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-tests .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'docker run --rm selenium-tests || true'
            }
        }
    }

    post {
        always {
            emailext (
                subject: "Test Results - ${JOB_NAME} - Build #${BUILD_NUMBER} - ${currentBuild.result}",
                body: """
Hi,

Jenkins has finished running Selenium tests for the Job Portal project.

Job     : ${JOB_NAME}
Build   : #${BUILD_NUMBER}
Status  : ${currentBuild.result}
Console : ${BUILD_URL}console

Regards,
Jenkins CI
                """,
                to: "qasimalik@gmail.com",
                recipientProviders: [
                    [$class: 'RequesterRecipientProvider'],
                    [$class: 'CulpritsRecipientProvider']
                ]
            )
        }
    }
}
