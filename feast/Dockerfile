FROM python:3.10.5-buster

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/usr/src/poetry_cache/ 

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

RUN pip install feast[redis]

COPY .tool-versions feature_store.yaml ./

