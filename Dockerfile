FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR /app

USER root
RUN apt-get update && apt-get install -y locales \
    && sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales

ENV LANG=ru_RU.UTF-8
ENV LC_ALL=ru_RU.UTF-8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["xvfb-run", "pytest", "-v", "-p", "no:xdist"]
