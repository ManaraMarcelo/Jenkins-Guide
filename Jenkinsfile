pipeline{
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerapp = docker.build("manaramarcelo/guia-jenkins:${env.BUILD_ID}",
                    '-f ./src/Dockerfile ./src')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        dockerapp.push('latest')
                        dockerapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Deploy no Kubernetes') {
            environment {
                tag_version = "${env.BUILD_ID}"
            }
            steps {

                // REMOVA withKubeConfig temporariamente e tente direto
                // O kubectl do sistema já deve estar configurado para o usuário jenkins
                /*sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                sh 'kubectl apply -f ./k8s/deployment.yaml'
                sh 'kubectl apply -f ./k8s/service.yaml'
                sh 'echo "Aplicação implantada no Kubernetes!"'*/

                withKubeConfig([credentialsId: 'kubeconfig']) {
                    // NOVO: Adiciona NO_PROXY para localhost E verbosidade ao kubectl
                    withEnv(["NO_PROXY=localhost,127.0.0.1"]) {
                        sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                        sh 'kubectl apply -f ./k8s/deployment.yaml -v=8' 
                        sh 'kubectl apply -f ./k8s/service.yaml -v=8'   
                        sh 'echo "Aplicação implantada no Kubernetes!"'

                        // NOVO: Teste de conectividade direta (para depuração)
                        sh 'curl -vvv https://127.0.0.1:6443/api/v1' 
                    }
                    /*sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                    sh 'kubectl apply -f ./k8s/deployment.yaml'
                    sh 'kubectl apply -f ./k8s/service.yaml'*/
                }
            }
        }
    }
}