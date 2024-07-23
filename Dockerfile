FROM python:3.10

WORKDIR /home/src

COPY . ./

RUN pip install -r requirements.txt

RUN apt-get update -y && \
    apt-get install python3-opencv -y 