FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update && apt-get install gcc libpq-dev python3-dev -y
RUN pip install --upgrade certifi
RUN pip install -r requirements.txt

COPY . .
