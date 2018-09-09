FROM python:3-alpine

ENV BIND_PORT 5001
ENV APP_REDIS_HOST redis
ENV APP_REDIS_PORT 6379

# MONGO
ENV APP_MONGO_HOST mongodb
ENV APP_MONGO_PORT 27017

# POSTGRES
ENV APP_POSTGRES_HOST postgresdb
ENV APP_POSTGRES_PORT 5432

EXPOSE $BIND_PORT

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache -r requirements.txt

CMD ["python", "app.py"]
