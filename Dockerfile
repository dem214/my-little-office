FROM python:3.9

# ENV PYTHONBUFFERED 1

RUN apt-get update
# Install GnuText
RUN apt-get install -y gettext

WORKDIR /usr/src/app

COPY  ./requirements ./requirements

RUN pip install --no-cache-dir -r requirements/dev.txt

