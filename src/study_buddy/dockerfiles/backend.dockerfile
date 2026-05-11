FROM python:3.13-slim

WORKDIR /app

COPY backend backend
COPY setup setup
COPY data data

ENV PYTHONPATH=/app

#install uv on the container
RUN pip install --no-cache-dir uv

WORKDIR /app/backend

RUN uv sync --no-dev

CMD ["uv","run","uvicorn","backend.api:app", "--host", "0.0.0.0", "--port","8000"]