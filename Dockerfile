FROM ubuntu

ENV PYTHONBUFFER=1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas && \
    pip3 install -i https://test.pypi.org/simple/ lambdata-n8mcdunna

