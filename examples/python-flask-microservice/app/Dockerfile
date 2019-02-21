FROM python:3.6

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

EXPOSE 9090
CMD ["python", "/app/app.py"]