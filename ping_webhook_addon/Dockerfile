ARG BUILD_FROM=ghcr.io/home-assistant/{arch}-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache iputils curl py3-requests

COPY run.sh /
COPY ping_webhook.py /

CMD [ "/run.sh" ]
