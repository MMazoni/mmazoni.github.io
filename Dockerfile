FROM python:3.8.9-alpine3.12

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

RUN pelican-themes -i theme/clean-blog
RUN pelican content

