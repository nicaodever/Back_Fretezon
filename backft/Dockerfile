FROM python:3.12.8-alpine

COPY . .

COPY requirements.txt ./

RUN  pip install --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apk add --update --no-cache postgresql-client &&\
    apk add --update --no-cache --virtual .tmp-buil-deps \
       build-base postgresql-dev musl-dev
EXPOSE 8080
