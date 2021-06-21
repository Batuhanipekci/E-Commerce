# pull official base image
FROM python:3.8-slim-buster

# create directories
RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system app && adduser app app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
ENV PYTHONPATH "/workspace:$PYTHONPATH"
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static_files

# set work directory
WORKDIR $APP_HOME

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME
USER app