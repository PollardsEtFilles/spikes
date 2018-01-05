FROM python:3.6

MAINTAINER PEF <peter@pollardsetfilles.com>

WORKDIR /code/

RUN pip install --upgrade pip

ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

ADD requirements-test.txt /code/requirements-test.txt
RUN pip install -r requirements-test.txt

RUN apt-get update
RUN apt-get install mysql-client -y

RUN rm -rf ~/.cache/pip

CMD [ "python" ]
