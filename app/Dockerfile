# -------------------APP
FROM python:3.8.6

RUN apt-get update && apt-get -y upgrade

COPY . ./app

# install dependencies

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r app/requirements.txt

# default command

WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=app.py

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]