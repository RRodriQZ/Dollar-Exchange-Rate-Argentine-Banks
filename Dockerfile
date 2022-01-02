FROM python:3.9-slim

RUN apt-get update

WORKDIR /dollar_exchange_rate_argentine_banks

COPY . /dollar_exchange_rate_argentine_banks

RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "application.py"]