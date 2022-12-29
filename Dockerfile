FROM python:3.10


RUN apt-get update && apt-get upgrade -y
COPY Scraper/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN  apt-get -y install netcat

WORKDIR /app

COPY Scraper .

EXPOSE 8000

COPY wait.sh wait.sh

RUN chmod +x wait.sh

ENTRYPOINT [ "./wait.sh" ]