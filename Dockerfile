FROM python:3.8

COPY . /opt/paitrainer

WORKDIR /opt/paitrainer

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "app:server", "-b", ":80"]