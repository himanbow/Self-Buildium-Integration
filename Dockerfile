FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

RUN adduser --disabled-password --gecos "" appuser

COPY pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        "fastapi>=0.103.0,<1" \
        "uvicorn>=0.22.0,<1" \
        "google-cloud-firestore>=2.11.0" \
        "google-cloud-secret-manager>=2.11.0" \
        "google-cloud-tasks>=2.10.0" \
        "google-api-core>=2.11.0" \
        "google-cloud-core>=2.3.0" \
        "pydantic>=2.0.0,<3" \
        "python-dateutil>=2.8.0" \
        "typing-extensions>=4.6.0" \
        "urllib3>=1.26.0,<2.1"

COPY my_app/ ./my_app/

USER appuser

CMD ["sh", "-c", "uvicorn my_app.webhooks.buildium_listener:app --host 0.0.0.0 --port ${PORT:-8080}"]
