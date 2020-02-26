FROM python:3.7-slim-stretch

ARG APP_DIR=/var/app
WORKDIR ${APP_DIR}
COPY requirements.txt ${APP_DIR}/requirements.txt
COPY gallery/ ${APP_DIR}/gallery/
RUN pip install -r requirements.txt
RUN python gallery/manage.py migrate
