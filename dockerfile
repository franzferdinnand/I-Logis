FROM python:3.10

RUN apt update \
&& mkdir /eCargo

WORKDIR /eCargo

COPY src ./src

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
&& pip install -r ./requirements.txt

EXPOSE 8008

CMD ["python", "src/manage.py", "runserver", "0:8000"]

#docker build -t ecargo .
#docker run --rm -it -d -p 8008:8000 --name ecargo_kont ecargo