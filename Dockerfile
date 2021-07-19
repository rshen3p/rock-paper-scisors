FROM python:alpine
COPY . /app
WORKDIR /app/src
RUN pip install pytest
RUN ["pytest", "-v"]
CMD python3 game.py