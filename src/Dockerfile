FROM python:3.8.12-slim

WORKDIR /app

RUN pip install --upgrade \
    pip

COPY requirements.txt ./
RUN pip install --requirement requirements.txt
COPY requirements.dev.txt ./
RUN pip install -r requirements.dev.txt

COPY . ./

# ENTRYPOINT [ "python", "main.py" ]
