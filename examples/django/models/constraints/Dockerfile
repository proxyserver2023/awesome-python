FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Dhaka
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /app
WORKDIR /app
RUN mkdir data
RUN mkdir code
ADD requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/code/
EXPOSE 8000
