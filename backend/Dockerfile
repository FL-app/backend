FROM python:3.11-slim

LABEL author='FLApp-Team'

LABEL maintainer='<https://github.com/FL-app>'

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y git

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
