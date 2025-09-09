FROM python:3.11-slim

# diretório de trabalho dentro do container
WORKDIR /app

# instala dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copia o resto do projeto
COPY . /app/

# expõe porta
EXPOSE 8000

# comando padrão para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]