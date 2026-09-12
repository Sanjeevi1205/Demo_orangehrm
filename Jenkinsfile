pipeline {

    agent any

    parameters {

        choice(
            name: 'TEST_TAG',
            choices: [
                '@create',
                '@update',
                '@delete',
                '@smoke',
                '@employee'
            ],
            description: 'Select Test Suite'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t orangehrm-framework .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                docker run --rm orangehrm-framework \
                --tags=${params.TEST_TAG} \
                --no-capture
                """
            }
        }
    }

    post {

        always {

            archiveArtifacts(
                artifacts: 'reports/**/*',
                allowEmptyArchive: true
            )

            archiveArtifacts(
                artifacts: 'screenshots/**/*',
                allowEmptyArchive: true
            )

            archiveArtifacts(
                artifacts: 'videos/**/*',
                allowEmptyArchive: true
            )
        }

        success {

            emailext(
                subject: "SUCCESS: OrangeHRM Automation Build #${BUILD_NUMBER}",
                body: """
                Build Status : SUCCESS

                Test Tag : ${params.TEST_TAG}

                Job Name : ${JOB_NAME}

                Build Number : ${BUILD_NUMBER}

                Build URL : ${BUILD_URL}
                """,
                to: "sanjeeviponnusamy051@gmail.com"
            )
        }

        failure {

            emailext(
                subject: "FAILED: OrangeHRM Automation Build #${BUILD_NUMBER}",
                body: """
                Build Status : FAILED

                Test Tag : ${params.TEST_TAG}

                Job Name : ${JOB_NAME}

                Build Number : ${BUILD_NUMBER}

                Build URL : ${BUILD_URL}

                Please check Jenkins logs and artifacts.
                """,
                to: "sanjeeviponnusamy051@gmail.com"
            )
        }
    }
}