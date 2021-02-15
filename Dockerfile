FROM python:3.7.9-buster

COPY . /home/app

WORKDIR /home/app
RUN pip install -r requirements.txt

CMD [ "gunicorn", "-b", ":8000", "config.wsgi" ]