FROM ubuntu:latest

FROM python:3.6.8

RUN mkdir /password-tester

WORKDIR /password-tester

COPY requirements.txt /password-tester/

COPY passwordtester.py /password-tester/

COPY testing.py /password-tester/

RUN pip install -r requirements.txt

CMD [ "python", "testing.py" ]

