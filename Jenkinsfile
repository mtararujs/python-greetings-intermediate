import hudson.model.*

pipeline {
    parameters {
        choice(name: 'DEPLOY_TO_PRODUCTION', choices: ['Yes', 'No'], description: "Parameter responsible for deploying to PRD or not")
        choice(name: "CUCUMBER_TAG", choices: ['No', 'Yes'], description: "To run by Cucumber tag?")
    }
    agent any
    triggers {
        pollSCM('*/1 * * * *')
    }
    stages {
        stage('build-app') {
            steps {
                echo "Build ${GIT_COMMIT}"
                sh "docker build -t mtararujs/python-greetngs-app:latest ."
                sh "docker push mtararujs/python-greetngs-app:latest"
            }
        }
        stage('deploy-dev') {
            steps {
                script{
                    deploy("dev")
                    load("commonFunctions.groovy").deploy("test groovy function")
                    if (params.DEPLOY_TO_PRODUCTION.equals("Yes")) {
                        echo "cucumber tags yes"
                    } else {
                        echo "cucumber tags no"
                    }
                }
            }
        }
        stage('test-dev') {
            parallel {
                stage('Test 1') {
                    steps {
                        echo "test parallel 1"
                        script{
                            test("DEV parallel 1")
                        }
                    }
                    post {
                        always {
                            echo "test parallel 1 post"
                        }
                    }
                }
                stage('Test 2') {
                    steps {
                        echo "test parallel 2"
                        script{
                            test("DEV parallel 2")
                        }
                    }
                    post {
                        always {
                            echo "test parallel 2 post"
                        }
                    }
                }
            }      
        }
        stage('Approval') {
            // no agent, so executors are not used up when waiting for approvals
            agent none
            steps {
                script {
                    def deploymentDelay = input id: 'Deploy', message: 'Deploy to production?', submitter: 'martins,admin', parameters: [choice(choices: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], description: 'Hours to delay deployment?', name: 'deploymentDelay')]
                    sleep time: deploymentDelay.toInteger(), unit: 'MINUTES'
                }
            }
        }
        stage('deploy-prd') {
            when {
                expression { params.DEPLOY_TO_PRODUCTION == 'Yes' }
            }
            steps {
                script{
                    deploy("prd")
                }
            }
        }
        stage('test-prd') {
            when {
                expression { params.DEPLOY_TO_PRODUCTION == 'Yes' }
            }
            steps {
                script{
                    test("PRD")
                }
            }
        }
    }
    post {
        always {
            script {
                echo '\033[1;34mStarting always stage...\033[0m'
            }
        }
        failure {
            script {
                echo 'Failure!'
                // slackSend channel: 'mobile_automation_updates',
                //         iconEmoji: ':red_circle:',
                //         color: "danger",
                //         message: "The build failed, please check the console log",
                //         tokenCredentialId: 'secret-slack-bot'
            }
        }
        aborted {
            sh 'docker rmi -f test'
        }
        cleanup {
            echo 'Cleanup Condition!'
            sh 'docker stop $(docker ps -a -q)'
            sh 'docker rm -f $(docker ps -a -q)'
        }
    }
}

def deploy(String environment){
   echo "Deployment of hello-app to ${environment} is starting.." 
//    sh "kubectl set image deployment hello-app-${environment} hello-app-${environment}-pod=mtararujs/python-greetngs-app:latest"
}

def test(String environment){
   echo "Testing of hello-app to ${environment} is starting"
//    sh "docker run --network=host -d -t --name api_test_executor_${environment} mtararujs/ubuntu_ruby_executor:latest"
//    try{
//         sh "docker exec api_test_executor_${environment} cucumber PLATFORM=${environment} --format html --out test-output/report.html"
//    }
//    finally{
//         sh "docker cp api_test_executor_${environment}:/usr/src/api-tests/test-output/report.html report_${environment}.html"
//         sh "docker rm -f api_test_executor_${environment}"
//         publishHTML([
//             allowMissing: false, 
//             alwaysLinkToLastBuild: false, 
//             keepAll: false, 
//             reportDir: '', 
//             reportFiles: "report_${environment}.html", 
//             reportName: "Test Report ${environment}", 
//             reportTitles: "Test Report ${environment}"])
//    }
                // catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                //     script {
                //         echo '\033[1;34mMoving Allure results files to WS... \033[0m'
                //         String allureResults = "/tmp/mobile-test/$BUILD_NUMBER/allure-results/"
                //         def allureResultsExist = fileExists allureResults

                //         if (allureResultsExist) {
                //             sh "cp -a $allureResults $env.WORKSPACE/Mobile/allure-results/"
                //             echo '\033[1;34mGenerating environment.properties file...\033[0m'
                //             echo "\033[1;34mPublishing Allure report...\033[0m"
                //             try {
                //                 sh "cp -a /tmp/mobile-test/$BUILD_NUMBER/environment.properties $env.WORKSPACE/Mobile/allure-results/"
                //             }
                //             catch (error) {
                //                 echo "Caught: ${error}"
                //             }
                //             allure jdk: '', properties: [[key: 'Platform', value: '${PLATFORM_NAME}'], [key: 'Downloaded From', value: '${DOWNLOAD_APP_FROM}'], [key: 'Build Number', value: '${BUILD_NUMBER}']], results: [[path: 'allure-results'], [path: '**/allure-results'], [path: './allure-results'], [path: './']]
                //         } else {
                //             echo '\033[1;31m /allure-results/ has not been found \033[0m'
                //             sh "exit 1"
                //         }
                //     }
                // }
}