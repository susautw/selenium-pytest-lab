FROM python:3.11.9-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    rm requirements.txt

COPY ./test /app/test


ENTRYPOINT [ "pytest", "-n", "4", "/app/test" ]