# Usa uma imagem oficial e leve do Python
FROM python:3.14-slim

# Define o diretório de trabalho padrão dentro do container
WORKDIR /app

# Copia primeiro o arquivo de requisitos para aproveitar o cache do Docker
COPY requirements.txt .

# Instala todas as dependências listadas no seu pip freeze
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante dos arquivos do projeto para dentro do container
COPY . .

# Porta padrão do Flask
EXPOSE 5000

# Executa o Flask garantindo que ele escute em todas as interfaces de rede (0.0.0.0)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]