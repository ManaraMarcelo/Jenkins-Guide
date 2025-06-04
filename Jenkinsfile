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
                sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                sh 'kubectl apply -f ./k8s/deployment.yaml' # Tente aplicar direto
                sh 'kubectl apply -f ./k8s/service.yaml'
                sh 'echo "Aplicação implantada no Kubernetes!"'

                //withKubeConfig([credentialsId: 'kubeconfig']) {
                //    sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                //    sh 'kubectl apply -f ./k8s/deployment.yaml'
                //    sh 'kubectl apply -f ./k8s/service.yaml'
                //}
            }
        }
    }
}