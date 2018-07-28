FROM python:latest

RUN mkdir /opt/app
WORKDIR /opt/app
ADD . /opt/app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/opt/app/app.py"]