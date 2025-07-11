FROM python:3.10-slim

WORKDIR /django-app

COPY django-app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY django-app/ .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]