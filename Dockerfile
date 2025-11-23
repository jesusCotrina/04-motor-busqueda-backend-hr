FROM python:3.11.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
