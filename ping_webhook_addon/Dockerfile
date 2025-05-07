ARG BUILD_FROM=ghcr.io/hassio-addons/base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache iputils curl

COPY run.sh /
COPY ping_webhook.py /

CMD [ "/run.sh" ]
