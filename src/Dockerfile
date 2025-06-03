# Usa uma imagem base oficial do Ubuntu
FROM ubuntu:latest

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Atualiza a lista de pacotes e instala o Python 3 e o pip (exemplo para uma aplicação Python)
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copia os arquivos da aplicação para o diretório de trabalho no contêiner
COPY . /app

# Instala as dependências da aplicação (se houver um requirements.txt, por exemplo)
RUN pip3 install -r requirements.txt

# Expõe a porta que a aplicação estará escutando (ex: 8000 para uma API)
EXPOSE 8000

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["python3", "app.py"]