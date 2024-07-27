FROM tiangolo/uwsgi-nginx-flask:python3.10.12-alpine
LABEL maintainer="ghostoflaboratory@gmail.com"
RUN apk --update add git
ENV STATIC_URL /static
ENV STATIC_PATH /myapp/static
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["run.py"]
EXPOSE 8000

