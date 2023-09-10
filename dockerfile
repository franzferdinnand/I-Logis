FROM python:3.10

RUN apt update \
&& mkdir /eCargo

WORKDIR /eCargo

COPY src ./src
COPY commands ./commands
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
&& pip install -r ./requirements.txt

CMD ["bash"]
