# Exemplo de app.py simples (em src/app.py)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá do Flask e do Jenkins!'

if __name__ == '__main__':
    # Gunicorn geralmente gerencia a porta em produção, mas para teste local
    # ou se não usar gunicorn, Flask pode rodar diretamente.
    # Para usar com Gunicorn, o CMD no Dockerfile pode ser:
    # CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
    app.run(host='0.0.0.0', port=8000)