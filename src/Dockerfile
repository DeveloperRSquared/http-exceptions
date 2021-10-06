FROM python:3.8.12-slim

WORKDIR /app

RUN pip install --upgrade \
    pip

# TODO(rikhil): run this pip install conditionally
RUN pip install -U twine setuptools wheel

COPY requirements.txt ./
RUN pip install --requirement requirements.txt
COPY requirements.dev.txt ./
RUN pip install --requirement requirements.dev.txt

COPY . ./
