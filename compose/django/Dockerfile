FROM python:3.11.3-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --fix-missing netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /app/start
RUN sed -i 's/\r$//g' /app/start
RUN chmod +x /app/start

COPY . .

ENTRYPOINT ["bash","/entrypoint"]