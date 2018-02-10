FROM python:3.6

MAINTAINER PEF <peter@pollardsetfilles.com>

RUN groupadd -g 1000 appuser && \
    useradd -rm -u 1000 -g appuser appuser

WORKDIR /home/appuser

COPY requirements.txt roles.yml /home/appuser/install/

RUN  pip install --upgrade pip \
  && pip install -r install/requirements.txt \
  && rm -rf ~/.cache/pip

USER appuser

RUN ansible-galaxy install -r install/roles.yml

CMD [ "ansible" ]
