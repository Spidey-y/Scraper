FROM python:3.10


# Magic happens
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && apt-get -y update && apt-get install -y google-chrome-stable && apt-get install -y unzip && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && apt-get -y install netcat

# Set display port as an environment variable
ENV DISPLAY=:99

COPY Scraper/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt


WORKDIR /app

COPY Scraper .

EXPOSE 8000

COPY wait.sh wait.sh

RUN chmod +x wait.sh

ENTRYPOINT [ "./wait.sh" ]