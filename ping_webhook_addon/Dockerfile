FROM ghcr.io/hassio-addons/base-python:12.2.7

# Install ping + curl (sono già dentro ma assicuriamoci)
RUN apk add --no-cache iputils curl

# Copy files
COPY run.sh /
COPY ping_webhook.py /

CMD [ "/run.sh" ]
