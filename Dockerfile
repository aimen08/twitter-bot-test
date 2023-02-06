FROM python:3.9

ADD . .

RUN pip install pyTelegramBotAPI python-dotenv loguru bs4 urllib3


CMD [ "python", "./twitter.py" ]