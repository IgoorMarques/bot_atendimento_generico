# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copie o código da aplicação
COPY . /app

# Exponha a porta da aplicação web
EXPOSE 5000

# Defina o comando para iniciar a aplicação
CMD ["python", "run.py"]
