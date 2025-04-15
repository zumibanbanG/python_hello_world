FROM public.ecr.aws/docker/library/python:3.13.0-slim-bookworm

WORKDIR /app

COPY pyproject.toml poetry.lock ./

ENV POETRY_REQUESTS_TIMEOUT=10800

RUN python -m pip install --upgrade pip && \
    pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root && \
    poetry cache clear --all pypi
    
COPY src /app/src

CMD ["poetry", "run", "python", "src/grpc/server.py"]

EXPOSE 50051