FROM pef/python3

LABEL maintainer="PEF <peter@pollardsetfilles.com>"

WORKDIR /code/

RUN pip install --upgrade pip

ADD main.py /code/
ADD env/env.sh /code/env/env.sh
ADD requirements.txt /code/requirements.txt
ENV PIP_EXTRA_INDEX_URL=http://dockerhost:8080/simple/
RUN pip install --trusted-host dockerhost -r requirements.txt

RUN rm -rf ~/.cache/pip

CMD [ "/code/main.py" ]
