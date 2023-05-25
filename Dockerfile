FROM python:3.11.3-alpine
LABEL authors="kachu"

RUN ["apk", "add", "ffmpeg"]
RUN ["pip", "install", "poetry"]

COPY poetry.lock .
COPY pyproject.toml .

RUN ["poetry", "install"]

COPY ./src/scpbot ./scpbot
ENV PYTHONPATH "$PYTHONPATH:./scpbot"

CMD ["poetry", "run", "python3", "-m", "scpbot"]