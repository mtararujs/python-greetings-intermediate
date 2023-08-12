pipeline{
    agent any
    triggers{
       pollSCM('*/1 * * * *') 
    }
    stages {
        stage('build-app'){
            steps {
                echo "Build python-greetings-app.."
                build("mtararujs/python-greetings-app:latest", "Dockerfile")
            }
        }
        stage('deploy-dev'){
            steps {
                script{
                    deploy("DEV")
                }
            }
        }
        stage('test-dev'){
            steps {
                script{
                    test("DEV")
                }
            }
        }
        stage('approval'){
            steps {
                echo "Manual approval before deployment to PROD.."
            }
        }
        stage('deploy-prod'){
            steps {
                script{
                    deploy("PROD")
                }
            }
        }
        stage('test-prod'){
            steps {
                script{
                    test("PROD")
                }
            }
        }
    }
    post {
        failure {
            script {
                echo "Pipeline failure.. Sending notification"
                // invoke discord plugin
            }
        }
        cleanup {
            echo "Cleanup procedure.."
            // potentially soem docker cleanup here as well
        }
    }
}

def build(String tag, String dockerfile){
    echo "Building ${tag} image based on ${dockerfile}"
    sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
    sh "docker build --no-cache -t ${tag} . -f ${dockerfile}"
    sh "docker push ${tag}"
}

def test(String environment){
    echo "Testing of python-greetings-app on ${environment} is starting.."
    // docker run .. 
    // docker exec
    // docker cp 
    // extract report logic
    // docker cleanup
}

def deploy(String environment){
    echo "Deployment of python-greetings-app on ${environment} is starting.."
    // kubectl set image ..
}