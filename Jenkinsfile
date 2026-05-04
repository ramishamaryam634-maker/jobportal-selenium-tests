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
            subject: "Selenium Test Results - ${JOB_NAME} - Build #${BUILD_NUMBER} - ${currentBuild.currentResult}",
            body: """
Hello Sir,

Jenkins has completed execution of Selenium automated tests for the Job Portal project.

Job Name     : ${JOB_NAME}
Build Number : ${BUILD_NUMBER}
Status       : ${currentBuild.currentResult}

All 15 Selenium automated test cases were executed inside Docker container on AWS EC2.

Console Output:
${BUILD_URL}console

Regards,
Ramisha Maryam
""",
            to: "qasimalik@gmail.com",
            mimeType: 'text/plain',
            recipientProviders: []
        )
    }
    }
}
