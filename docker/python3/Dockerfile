FROM python:3

MAINTAINER PEF <peter@pollardsetfilles.com>

WORKDIR /code/

RUN pip install --upgrade pip

ADD python3/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

ADD requirements-test.txt /code/requirements-test.txt
RUN pip install -r requirements-test.txt

RUN rm -rf ~/.cache/pip
