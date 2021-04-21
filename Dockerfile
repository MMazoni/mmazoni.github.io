FROM python:3.8-buster

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

RUN pelican-themes -i theme/clean-blog
RUN pelican content
RUN git config --global user.name 'Matheus Mazoni'
RUN git config --global user.email 'mmazoni.andrade@gmail.com'