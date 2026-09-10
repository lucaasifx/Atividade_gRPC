# Imagem do python
FROM python:3.12-slim

# caminho relativo do projeto na arvore de arquivos do container
WORKDIR /app

# Copia todos os arquivos do projeto para a pasta /app do container
COPY . /app

# Instala as dependências listadas no requirements.txt
RUN pip install -r requirements.txt

# Porta usada pelo serviço gRPC
EXPOSE 32768

# Roda o servidor
# -u se não não printa no terminalkkk (unbuffered)
CMD ["python", "-u", "server.py"]
