pipeline{
    agent any
    triggers{
       pollSCM('*/1 * * * *') 
    }
    stages {
        stage('build-app'){
            steps {
                echo "Build python-greetings-app"
            }
        }
        stage('deploy-dev'){
            steps {
                echo "Deploying python-greetings-app to DEV.."
            }
        }
        stage('test-dev'){
            steps {
                echo "Testing python-greetings-app on DEV.. "
            }
        }
        stage('approval'){
            steps {
                echo "Manual approval before deployment to PROD.."
            }
        }
        stage('deploy-prod'){
            steps {
                echo "Deploying python-greetings-app to PROD.."
            }
        }
        stage('test-prod'){
            steps {
                echo "Testing python-greetings-app on PROD.. "
            }
        }
    }
}