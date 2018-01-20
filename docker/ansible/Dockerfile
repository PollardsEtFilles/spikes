FROM python:3.6-slim

MAINTAINER PEF <peter@pollardsetfilles.com>

WORKDIR /code/

COPY requirements.txt roles.yml /code/

RUN  pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf ~/.cache/pip

RUN ansible-galaxy install -r roles.yml

CMD [ "ansible" ]
