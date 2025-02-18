FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SERVER_ADDRESS=0.0.0.0:8000

EXPOSE 8000

CMD ["sh", "-c", "until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT; do echo waiting for database; sleep 2; done && cd PulseBackend && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
