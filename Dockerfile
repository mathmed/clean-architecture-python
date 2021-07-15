FROM python:3.8

ENV APP_PORT=80

RUN mkdir /home/api
COPY . /home/api
RUN cd /home/api && pip install -r requirements.txt

CMD [ "python3", "/home/api/main.py" ]
