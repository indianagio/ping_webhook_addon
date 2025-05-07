ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip curl iputils

COPY run.sh /
COPY ping_webhook.py /
COPY requirements.txt /

RUN pip3 install -r /requirements.txt

CMD [ "/run.sh" ]
