# Stage 1 - Build requirements
FROM python:3.12-slim-bullseye AS base-build

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
        pkg-config \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN mkdir /app/src

RUN pip install uv -U
COPY ./requirements /app/requirements
RUN uv pip install --system -r requirements/base.txt

# Stage 2 - Make image
FROM python:3.12-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps \
        vim \
        mime-support \
        postgresql-client \
        gettext \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./bin/start_http_server.sh /start.sh

COPY --from=base-build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=base-build /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY ./src /app/src

RUN useradd -M -u 1000 notifications && chown -R notifications:notifications /app

# drop privileges
USER notifications

EXPOSE 8000