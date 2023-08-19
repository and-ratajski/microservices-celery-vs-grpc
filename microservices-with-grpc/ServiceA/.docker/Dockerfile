FROM python:3.10-bullseye AS base
RUN python -m pip install --upgrade pip
WORKDIR /app

COPY ./.docker/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app .

ENTRYPOINT ["python", "app.py"]
