# Dockerfile
FROM python:3.9-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    net-tools \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY scripts/ ./scripts/
COPY logs/ ./logs
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta para o serviço REST
EXPOSE 5000

# Comando padrão para iniciar o serviço REST
CMD ["python", "scripts/rest_service.py"]