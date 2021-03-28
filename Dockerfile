FROM python:3.8.2-slim-buster
RUN apt-get update && apt-get install -y libpq-dev gcc
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt