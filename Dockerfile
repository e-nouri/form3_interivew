FROM python:2.7-onbuild
MAINTAINER Nouri NOURI

WORKDIR /app/

COPY run.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./run.py"]