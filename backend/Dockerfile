FROM python:3.10.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg dependencies
  build-essential \
  libpq-dev \
  # pytest-postgres dependencies
  python3-dev \
  postgresql

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY . /app

RUN useradd -m -d /app -s /bin/bash appuser \
    && chown -R appuser:appuser /app/*

USER appuser

WORKDIR /app

CMD ["uvicorn", "planit.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "/app"]