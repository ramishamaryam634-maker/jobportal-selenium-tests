pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/ramishamaryam634-maker/jobportal-selenium-tests.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-tests .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'docker run --rm selenium-tests'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished Successfully'
        }
    }
}
