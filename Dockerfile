FROM python:3.7

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=server
ENV FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src /usr/src/app

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
