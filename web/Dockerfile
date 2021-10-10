FROM python:3.7

RUN mkdir -p /home/project/web
WORKDIR /home/project/web
COPY Pipfile /home/project/web
COPY Pipfile.lock /home/project/web
RUN pip install pipenv gunicorn
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pipenv install numpy opencv-python imutils
RUN pipenv install --system --deploy

COPY . /home/project/web
