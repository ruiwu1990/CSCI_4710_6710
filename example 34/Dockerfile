FROM ubuntu:16.04
MAINTAINER Rui Wu
LABEL description="This is for programming style checker."

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential pylint default-jre default-jdk

#copy source code
COPY . /programming_checker
WORKDIR /programming_checker
ENV PYTHONPATH /programming_checker


#install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENV CHECKER_PORT 80
ENV CHECKER_HOST 0.0.0.0
EXPOSE ${CHECKER_PORT}

CMD python cct_main.py -p 5000 --threaded
