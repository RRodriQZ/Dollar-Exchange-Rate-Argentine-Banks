FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip install "poetry==1.3.2"

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt
