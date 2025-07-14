FROM python:3.10-slim

WORKDIR /django-app

# Copy requirements file first
COPY python-api/django-app/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY python-api/django-app/ .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
