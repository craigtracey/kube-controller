FROM python:2-alpine3.8

RUN apk update && apk add git

WORKDIR /tmp/
COPY kube_controller /tmp/kube_controller/
COPY .git /tmp/.git/
COPY setup.py /tmp/setup.py
COPY setup.cfg /tmp/setup.cfg
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt
RUN python setup.py install
