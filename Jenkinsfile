pipeline{
    agent any

    stages{
        stage('Build Docker Image'){
            steps{
                sh 'echo "Executando o comando Dokcer Build"'
            }
        }
        stage('Push Docker Image'){
            steps{
                sh 'echo "Executando o comando Dokcer Push"'
            }
        }
        stage('Deploy no Kubernetes'){
            steps{
                sh 'echo "Executando o comando Kubectl Apply"'
            }
        }
    }
}