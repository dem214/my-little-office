FROM python:3.9

ENV PYTHONBUFFERED 1

RUN apt-get update
# Install GnuText
RUN apt-get install -y gettext

RUN useradd -ms /bin/bash my-little-office

USER my-little-office

WORKDIR /home/my-little-office

COPY --chown=my-little-office ./requirements/ /home/my-little-office/

RUN pip install -r /home/my-little-office/dev.txt
