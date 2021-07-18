FROM python:alpine
COPY . /app
WORKDIR /app/src
CMD python3 game.py