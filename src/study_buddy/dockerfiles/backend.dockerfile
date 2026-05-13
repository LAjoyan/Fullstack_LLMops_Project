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
