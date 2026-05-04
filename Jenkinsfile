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
                // || true means: even if tests fail, pipeline continues to email stage
                sh 'docker run --rm selenium-tests || true'
            }
        }
    }

    post {
        always {
            emailext (
                subject: "Test Results - Build #${BUILD_NUMBER} - ${currentBuild.result}",
                body: """
Hi,

Jenkins pipeline has finished running Selenium tests.

Job     : ${JOB_NAME}
Build   : #${BUILD_NUMBER}
Status  : ${currentBuild.result}
Link    : ${BUILD_URL}console

Regards,
Jenkins
                """,
                recipientProviders: [
                    [$class: 'RequesterRecipientProvider'],
                    [$class: 'CulpritsRecipientProvider']
                ]
            )
        }
    }
}
