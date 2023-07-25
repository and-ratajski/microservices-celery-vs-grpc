FROM python:3.10-bullseye AS base
RUN python -m pip install --upgrade pip
WORKDIR /app

COPY ./.docker/dev/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app .

ENTRYPOINT ["celery", "-A", "tasks", "worker"]
