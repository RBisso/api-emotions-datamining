FROM python:3.7.9-buster

COPY . /home/app

WORKDIR /home/app
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]