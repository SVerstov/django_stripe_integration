FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8080

CMD python manage.py runserver 0.0.0.0:8080

# docker build . -t stripe-django-v0.1
# docker run -p 8080:8080 stripe-django-v0.1
