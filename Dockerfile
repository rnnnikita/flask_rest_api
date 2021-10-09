FROM python:3.9-bullseye

RUN apt-get update -y

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]
