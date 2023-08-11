pipeline {
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
                }
            }
        }
        stage('test-dev') {
            steps {
                script{
                    test("DEV")
                }
            }
        }
        stage('deploy-prd') {
            steps {
                script{
                    deploy("prd")
                }
            }
        }
        stage('test-prd') {
            steps {
                script{
                    test("PRD")
                }
            }
        }
    }
}

def deploy(String environment){
   echo "Deployment of hello-app to ${environment} is starting.." 
   sh "kubectl set image deployment hello-app-${environment} hello-app-${environment}-pod=mtararujs/python-greetngs-app:latest"
}

def test(String environment){
   echo "Testing of hello-app to ${environment} is starting"
   sh "docker run --network=host -d -t --name api_test_executor_${environment} mtararujs/ubuntu_ruby_executor:latest"
   try{
        sh "docker exec api_test_executor_${environment} cucumber PLATFORM=${environment} --format html --out test-output/report.html"
   }
   finally{
        sh "docker cp api_test_executor_${environment}:/usr/src/api-tests/test-output/report.html report_${environment}.html"
        sh "docker rm -f api_test_executor_${environment}"
        publishHTML([
            allowMissing: false, 
            alwaysLinkToLastBuild: false, 
            keepAll: false, 
            reportDir: '', 
            reportFiles: "report_${environment}.html", 
            reportName: "Test Report ${environment}", 
            reportTitles: "Test Report ${environment}"])
   }
}