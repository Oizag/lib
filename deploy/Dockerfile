FROM python:3.11-alpine

WORKDIR /var/www/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install global packages
RUN apk update \
    && apk upgrade \
    && apk add --no-cache  \
    git \
    postgresql-dev \
    bash \
    libc-dev \
    libffi-dev \
    mariadb-dev \
    curl \
    jpeg-dev \
    zlib-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev \
    python3-dev \
    make

RUN  fc-cache -f

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH="${PATH}:/etc/poetry/bin"

COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install

COPY . .


