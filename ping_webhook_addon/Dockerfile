ARG BUILD_FROM=ghcr.io/home-assistant/{arch}-base-python:3.12
FROM ${BUILD_FROM}

RUN apk add --no-cache iputils curl

COPY run.sh /
COPY ping_webhook.py /

CMD [ "/run.sh" ]
