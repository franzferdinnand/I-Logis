FROM python:3.10-slim

RUN apt update \
&& mkdir /eCargo

WORKDIR /eCargo

COPY src ./src
COPY commands ./commands
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
&& pip install -r ./requirements.txt

EXPOSE 8008

CMD ["bash"]
